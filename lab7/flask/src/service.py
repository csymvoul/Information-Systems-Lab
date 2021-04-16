from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from flask import Flask, request, jsonify, redirect, Response
#Monitoring
from prometheus_client import CollectorRegistry
from prometheus_client.exposition import CONTENT_TYPE_LATEST, generate_latest
from prom import Collector
from mon import Monitoring

import json, os, sys, psutil, time, platform, random 
sys.path.append('./data')
import prepare_data 
from metricsender import Routine 

# Connect to our local MongoDB

mongodb_hostname = os.environ.get("MONGO_HOSTNAME","localhost")
hostname = os.environ.get("HOSTNAME",platform.node())
replicas = os.environ.get("REPLICAS","main")

n_retries = 10
index = 0
client = None 
while index < n_retries:
    try:
        client = MongoClient('mongodb://'+mongodb_hostname+':27017/')
        break 
    except:
        print("Connection failed, process will sleep for 5s")
        time.sleep(5)
        index +=1
if client == None:
    raise ConnectionError("Could not establish connection to the database")

monitoring = Monitoring("flask",replicas)
# Choose InfoSys database
db = client['InfoSys']
students = db['Students']
port = 5000
# Initiate Flask App
app = Flask(__name__)
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.INFO)
#Global variable 
total_request = 0
served_request = 0
start_time = time.time()
list_request_response = []

#haproxy add parameter
def add_server_name():
    entry = "  server "+replicas+" "+hostname+":"+str(port)+ " check\n"
    try:
        file = open("haproxy.cfg","a")
        file.write(entry)
        file.close()
        log.info("Server parameter added to the proxy")
    except Exception as e:
        print(e)
# server apache1 ${APACHE_1_IP}:${APACHE_EXPOSED_PORT} check
#service discovery
def file_sd():
    file_content = None 
    file = None 
    try:
        file = open("targets.json","rw")
        file_content = file.read()
    except Exception as e:
        print(e)
        return None 
    if file_content != None:
        print(type(file_content))
        _json = json.loads(file_content)
        for target in _json:
            if hostname+":"+str(port) in target["targets"]:
                log.info("Configuration already exists")
                return None 
        my_parameters = {'targets':[hostname+":"+str(port)],'labels':{'hostname': hostname}}
        _json.append(my_parameters)
        file.truncate(0)
        file.write(json.dumps(_json))
        file.close()
        add_server_name()
        log.info("Discory parameters added")

#check if data existence
def check_data():
    try:
        if students.find({}).count() == 0:
            prepare_data.insert_all()
    except Exception as e:
        print(e)
        raise e
# Insert Student
# Create Operation
@app.route('/insertstudent', methods=['POST','GET'])
def insert_student():
    # Request JSON data
    global list_request_response, total_request, served_request
    total_request +=1
    start_time = time.time()
    data_param = request.args.get('param') 
    data = None 
    try:
        data = json.loads(data_param)
    except Exception as e:
        print(e)
        return Response("bad json content",status=500,mimetype='application/json')
    if data == None:
        return Response("bad request",status=500,mimetype='application/json')
    if not "name" in data or not "yearOfBirth" in data or not "email" in data:
        return Response("Information incompleted",status=500,mimetype="application/json")
    if students.find({"email":data["email"]}).count() == 0 :
        student = {"email": data['email'], "name": data['name'],  "yearOfBirth":data['yearOfBirth']}
        # Add student to the 'students' collection
        students.insert_one(student)
        response_time = time.time() - start_time
        list_request_response.append(response_time)
        served_request +=1
        return Response(data['name']+" was added to the MongoDB",status=200,mimetype='application/json') 
    else:
        response_time = time.time() - start_time
        list_request_response.append(response_time)
        served_request +=1
        return Response("A user with the given email already exists",status=200,mimetype='application/json')

# Read Operations
# Get all students
@app.route('/getallstudents', methods=['GET'])
def get_all_students():
    global list_request_response, total_request, served_request
    total_request +=1
    start_time = time.time()
    iterable = students.find({})
    output = []
    for student in iterable:
        student['_id'] = None 
        output.append(student)
    response_time = time.time() - start_time
    list_request_response.append(response_time)
    served_request +=1
    return jsonify(output)

# Get the number of all the students in the DB 
@app.route('/getstudentcount', methods=['GET'])
def get_students_count():
    global list_request_response, total_request, served_request
    total_request +=1
    start_time = time.time()
    number_of_students = students.find({}).count()
    response_time = time.time() - start_time
    list_request_response.append(response_time)
    served_request +=1
    return jsonify({"Number of students": number_of_students})
    
# Find student by email
@app.route('/getstudent/<string:email>', methods=['GET'])
def get_student_by_email(email):
    global list_request_response, total_request, served_request
    total_request +=1
    start_time = time.time()
    if email == None:
        served_request +=1
        return Response("Bad request", status=500, mimetype='application/json')
    student = students.find_one({"email":email})
    response_time = time.time() - start_time
    list_request_response.append(response_time)
    if student !=None:
        student = {'name':student["name"],'email':student["email"], 'yearOfBirth':student["yearOfBirth"]}
        served_request +=1
        return jsonify(student)
    served_request +=1
    return Response('No student found with that email '+ email +' was found',status=500,mimetype='application/json')
    # return jsonify({"student":student})
@app.route('/deletestudent/<string:email>', methods=['DELETE'])
def delete_student(email):
    global total_request, served_request
    total_request +=1
    if email == None:
        served_request +=1
        return Response("Bad request", status=500, mimetype='application/json')
    students.delete_one({"email": email})
    served_request +=1
    return Response("Student deleted successfuly", status=200, mimetype='application/json')

def collectMetrics():
    process = psutil.Process(os.getpid())
    memory_usage = process.memory_info().rss
    processor_usage = psutil.cpu_percent()

    global total_request, start_time, list_request_response, served_request
    avg_response_time = 0
    if len(list_request_response) == 0:
        avg_response_time = 0
    else:
        avg_response_time = sum(list_request_response)*1000/len(list_request_response)
    request_rate = int(total_request/(time.time() - start_time))
    served_rate = int(served_request/(time.time() - start_time))
    kpi = None 
    #if request_rate == 0:
    #    kpi = 100
    #else:
    #    kpi = int((served_rate*100)/10)
    kpi = (200.0/avg_response_time)*100
    if kpi > 100:
        kpi = 100 
    monitoring.setMetric("kpi",kpi)
    monitoring.setMetric("performance",kpi)
    monitoring.setMetric("response_time",avg_response_time)
    monitoring.setMetric("memory",memory_usage)
    monitoring.setMetric("cpu_usage",processor_usage)
    monitoring.setMetric("request_rate",request_rate)
    monitoring.setMetric("served_request",served_request)
    monitoring.setMetric("lost_request",abs(total_request-served_request))
    del list_request_response[:]
    #monitoring.increment('request')
    metrics = monitoring.getMetrics()
    app_name, replicas = monitoring.getIdentity()
    result = {'metrics': metrics,'labels': {'application':app_name,'replica':replicas,'hostname': hostname}}
    start_time = time.time()
    total_request = 0
    served_request = 0
    return result
    
#routine = Routine(collectMetrics)
#routine.start()

#Monitoring endpoint 
@app.route('/metrics',methods=['GET'])
def metrics():
    process = psutil.Process(os.getpid())
    memory_usage = process.memory_info().rss
    processor_usage = psutil.cpu_percent()

    global total_request, start_time, list_request_response, served_request
    avg_response_time = 0
    if len(list_request_response) == 0:
        avg_response_time = 0
    else:
        avg_response_time = sum(list_request_response)*1000/len(list_request_response)
    request_rate = int(total_request/(time.time()-start_time))
    served_rate = int(served_request/(time.time() - start_time))
    kpi = None 
    if avg_response_time < 1:
        kpi = 0
    else:
        kpi = served_rate/avg_response_time
    monitoring.setMetric("kpi",kpi)
    monitoring.setMetric("performance",kpi)
    monitoring.setMetric("response_time",avg_response_time)
    monitoring.setMetric("memory",memory_usage)
    monitoring.setMetric("cpu_usage",processor_usage)
    monitoring.setMetric("request_rate",request_rate)
    monitoring.setMetric("served_request",served_request)
    monitoring.setMetric("lost_request",abs(total_request-served_request))
    del list_request_response[:]
    #monitoring.increment('request')
    metrics = monitoring.getMetrics()
    app_name, replicas = monitoring.getIdentity()
    registry = Collector([app_name,replicas],metrics=metrics)
    collected_metric = generate_latest(registry)
    start_time = time.time()
    total_request = 0
    served_request = 0
    #monitoring.increment('request_success')
    return Response(collected_metric,status=200,mimetype=CONTENT_TYPE_LATEST)

# Run Flask App
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)

from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from flask import Flask, request, jsonify, redirect, Response
import json

# Connect to our local MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Choose InfoSys database
db = client['InfoSys']
students = db['Students']
testing = db['Test-Collection']
testing.insert_one({'student': '123123'})
# Initiate Flask App
app = Flask(__name__)

# Insert Student
# Create Operation
@app.route('/insertstudent', methods=['POST'])
def insert_student():
    # Request JSON data
    data = None 
    try:
        data = json.loads(request.data)
    except Exception as e:
        return Response("bad json content",status=500,mimetype='application/json')
    if data == None:
        return Response("bad request",status=500,mimetype='application/json')
    if not "name" in data or not "yearOfBirth" in data or not "email" in data:
        return Response("Information incompleted",status=500,mimetype="application/json")
    
    if students.find({"email":data["email"]}).count() == 0 :
        student = {"email": data['email'], "name": data['name'],  "yearOfBirth":data['yearOfBirth']}
        # Add student to the 'students' collection
        students.insert_one(student)
        return Response(data['name']+" was added to the MongoDB",status=200,mimetype='application/json') 
    else:
        return Response("A user with the given email already exists",status=200,mimetype='application/json')

# Read Operations
# Get all students
@app.route('/getallstudents', methods=['GET'])
def get_all_students():
    iterable = students.find({})
    output = []
    for student in iterable:
        student['_id'] = None 
        output.append(student)
    return jsonify(output)

# Get the number of all the students in the DB 
@app.route('/getstudentcount', methods=['GET'])
def get_students_count():
    number_of_students = students.find({}).count()
    return jsonify({"Number of students": number_of_students})
    
# Find student by email
@app.route('/getstudent/<string:email>', methods=['GET'])
def get_student_by_email(email):
    if email == None:
        return Response("Bad request", status=500, mimetype='application/json')
    student = students.find_one({"email":email})
    if student !=None:
        student = {'name':student["name"],'email':student["email"], 'yearOfBirth':student["yearOfBirth"]}
        return jsonify(student)
    return Response('No student found with that email '+ email +' was found',status=500,mimetype='application/json')
    # return jsonify({"student":student})

# Update Operation (PUT)
# Find student by email and update
@app.route('/updatestudent/<string:email>', methods=['PUT'])
def update_student(email):
    if email == None:
        return Response({"Bad request"},status=500,mimetype="application/json")
    
    student = students.find_one({"email":email})
    if student == None:
        return Response('No student found with that email '+ email +' was found',status=500,mimetype='application/json')

    try: 
        student = students.update_one({"email":email}, 
        {"$set":
            {
                "name":request.form["name"], 
                "email" : request.form["email"], 
                "yearOfBirth" : int(request.form["yearOfBirth"])
            }
        })
        student = students.find_one({"email":email})
        student = {'name':student['name'], 'email':student['email'], 'yearOfBirth':student['yearOfBirth']}
        return jsonify(student), 200
    except Exception as e:
        return Response({'User could not be updated'},status=500,mimetype='application/json')

# Update Operation (PATCH)
# Find student by email and update its name 
@app.route('/updatename/<string:email>', methods=['PATCH'])
def update_name(email):
    if email == None:
        return Response({"Bad request"},status=500,mimetype="application/json")
    
    student = students.find_one({"email":email})
    if student == None:
        return Response('No student found with that email '+ email +' was found',status=500,mimetype='application/json')

    try: 
        student = students.update_one({"email":email}, 
        {"$set":
            {
                "name" : request.form["name"]
            }
        })
        return Response({'Entry changed successfuly \n"name":"'+request.form["name"]+'"'},status=200,mimetype='application/json')
    except Exception as e:
        return Response({'User could not be updated'},status=500,mimetype='application/json')

@app.route('/deletestudent/<string:email>', methods=['DELETE'])
def delete_student(email):
    if email == None:
        return Response("Bad request", status=500, mimetype='application/json')
    students.delete_one({"email": email})
    return Response("Student deleted successfuly", status=200, mimetype='application/json')

# Run Flask App
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

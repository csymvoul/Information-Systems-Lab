from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
import json, uuid, time,requests 
from termcolor import colored
import random

# Connect to our local MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Choose database
db = client['InfoSys']

# Choose collections
students = db['Students']
users = db['Users']

server = "http://localhost:5000"

test_status_map = {}
logged_uuid = None 
student_email = None 

class Callback():
    @staticmethod
    def handler(status, response, _type, other_data):
        global logged_uuid
        if not status:
            print(colored(_type + " Failed","red"), colored("output ->","white"), colored(response, "red"))
            test_status_map[_type] = False 
            return False 

        if _type == 'create_user':
            if response.status_code == 200:
                print(colored(_type +" Passed", "green"))
                test_status_map[_type] = True 
                return True
            test_status_map[_type] = False 
            return False 

        if _type == 'duplicate_user':
            if response.status_code == 400:
                print(colored(_type+ " Success"), "green")
                return True 
            print(colored(_type+" Failed, the expected response code is 400, got {0}".format(response.status_code),"red"))
            return False 

        if _type == 'login':
            if 'uuid' in json.loads(response.text) and response.status_code == 200:
                logged_uuid = json.loads(response.text)['uuid']
                print(colored(_type+" test passed"),"green")
                test_status_map[_type] = True 
                return True 
            print(colored(_type+" test failed","red"))
            return False 
        if _type == 'get_student':
            if response.status_code != 200:
                print(colored(_type+" test, the expected status code is 200, got {0}".format(response.status_code),"red"))
                test_status_map[_type] = False 
                return False 
            try:
                if json.loads(response.text)['email'] == other_data['email']:
                    print(colored(_type+" test passed","green"))
                    test_status_map[_type] = True 
                    return True 
                test_status_map[_type] = False 
                return False 
            except Exception as e:
                print(colored(_type+" test failed","red"))
                test_status_map[_type] = False 
                return False 
            
        if _type == 'get_thirties':
            if response.status_code != 200:
                print(colored(_type+" test, the expected status code is 200, got {0}".format(response.status_code),"red"))
                test_status_map[_type] = False 
                return False 
            try:
                students = json.loads(response.text)
                for student in students:
                    if student['yearOfBirth'] != 1991:
                        test_status_map[_type] = False 
                        print(colored(_type+" test failed","red"))
                        return False 
                print(colored(_type+" test passed","green"))
                test_status_map[_type] = True 
                return True 
            except Exception as e:
                test_status_map[_type] = False 
                print(colored(_type+" test failed","red"))
                return False 
        if _type == 'get_oldy':
            if response.status_code != 200:
                print(colored(_type+" test, the expected status code is 200, got {0}".format(response.status_code),"red"))
                test_status_map[_type] = False 
                return False 
            try:
                students = json.loads(response.text)
                for student in students:
                    if student['yearOfBirth'] > 1991:
                        test_status_map[_type] = False 
                        print(colored(_type+" test failed","red"))
                        return False 
                print(colored(_type+" test passed","green"))
                test_status_map[_type] = True 
                return True 
            except Exception as e:
                test_status_map[_type] = False 
                print(colored(_type+" test failed","red"))
                return False
        if _type == "get_student_addresses":
            if response.status_code == 200:
                try:
                    if 'street' in json.loads(response.text):
                        print(colored(_type+" test Passed","green"))
                        test_status_map[_type] = True 
                        return True 
                    else:
                        print(colored(_type+" test Failed","red"))
                        test_status_map[_type] = False
                        return False 
                except Exception as e:
                    print(colored(_type+" test Failed -> error : " + e,"red"))
                    test_status_map[_type] = False
                    return False

            print(colored(_type+" test Failed -> error : " + e,"red"))
            test_status_map[_type] = False
            return False 
        if _type == "delete_student":
            if response.status_code == 200:
                print(colored(_type+" test passed","green"))
                test_status_map[_type] = True
                return True 
            else:
                print(colored(_type+" test Failed -> error : " + e,"red"))
                test_status_map[_type] = False
                return False

        if _type == "add_courses":
            if response.status_code == 200:
                print(colored(_type+" test passed","green"))
                test_status_map[_type] = True
                return True 
            else:
                print(colored(_type+" test Failed","red"))
                test_status_map[_type] = False
                return False

        if _type == "get_passed_courses":
            if response.status_code == 200:
                try:
                    _json = json.loads(response.text)
                    courses = list(_json.keys())
                    if "course 1" in courses and "course 3" in courses:
                        print(colored(_type+" test passed","green"))
                        test_status_map[_type] = True
                        return True 
                    else:
                        print(colored(_type+" test Failed","red"))
                        test_status_map[_type] = False
                        return False
                except Exception as e:
                    print(colored(_type+" test Failed -> error : " + e,"red"))
                    test_status_map[_type] = False
                    return False
                print(colored(_type+" test passed","green"))
                test_status_map[_type] = True
                return True 
            else:
                print(colored(_type+" test Failed -> error : " + e,"red"))
                test_status_map[_type] = False
                return False
            

def sendRequest(method,url, data, headers, callback,callback_type, other_data):
    if method == 'GET':
        try:
            response = requests.get(url,params=json.dumps(data), headers=headers)
            callback(True,response,callback_type,other_data)
        except Exception as e:
            return callback(False, e, callback_type,other_data)

    if method == 'POST':
        try:
            response = requests.post(url,data=json.dumps(data), headers=headers)
            callback(True,response,callback_type,other_data)
        except Exception as e:
            callback(False, e, callback_type,other_data)

    if method == 'DELETE':
        try:
            response = requests.get(url, data=json.dumps(data),params=json.dumps(data), headers=headers)
            callback(True,response,callback_type,other_data)
        except Exception as e:
            callback(False, e,callback_type,other_data)
    if method == 'PATCH':
        try:
            response = requests.patch(url,data=json.dumps(data), headers=headers)
            callback(True,response, callback_type,other_data)
        except Exception as e:
            callback(False, e, callback_type,other_data)

def createUser():
    data = {'username': 'tester', 'password': 'tester-1'}
    url = server + '/createUser'
    sendRequest('POST',url, data, {'Content-Type':'application/json'}, Callback.handler, 'create_user',{}) 
    sendRequest('POST',url, data, {'Content-Type':'application/json'}, Callback.handler, 'duplicate_user',{}) 

def login():
    data = {'username': 'tester', 'password': 'tester-1'}
    url = server + '/login'
    sendRequest('POST',url, data, {'Content-Type':'application/json'}, Callback.handler, 'login',{}) 

def getStudent():
    emails = readEmails()
    index = random.randint(0, len(emails)-1)
    url = server + '/getStudent'
    params = {'email': emails[index]}
    headers = {'Content-Type':'application/json','authorization': logged_uuid}
    sendRequest('GET',url, params, {'Content-Type':'application/json'}, Callback.handler, 'get_student',params) 

def getThirties():
    url = server + '/getStudents/thirties'
    params = {}
    headers = {'Content-Type':'application/json','authorization': logged_uuid}
    sendRequest('GET',url, params, {'Content-Type':'application/json'}, Callback.handler, 'get_thirties',{}) 

def getOldies():
    url = server + '/getStudents/oldies'
    params = {}
    headers = {'Content-Type':'application/json','authorization': logged_uuid}
    sendRequest('GET',url, params, {'Content-Type':'application/json'}, Callback.handler, 'get_oldy',{}) 

def getStudentAdresses():
    url = server + '/getStudentAddress'
    emails = readEmails()
    index = random.randint(0, len(emails)-1)
    params = {'email': emails[index]}
    headers = {'Content-Type':'application/json','authorization': logged_uuid}
    sendRequest('GET',url, params, {'Content-Type':'application/json'}, Callback.handler, 'get_student_addresses',{}) 

def deleteStudent():
    url = server + '/deleteStudent'
    emails = readEmails()
    index = random.randint(0, len(emails)-1)
    params = {'email': emails[index]}
    headers = {'Content-Type':'application/json','authorization': logged_uuid}
    sendRequest('DELETE',url, params, {'Content-Type':'application/json'}, Callback.handler, 'delete_student',{}) 

def addCourses():
    global student_email
    url = server + '/addCourses'
    emails = readEmails()
    index = random.randint(0, len(emails)-1)
    student_email = emails[index]
    data = { "email": student_email,"courses": [{"course 1": 10}, {"course 2": 3 }, {"course 3": 8}]} 
    headers = {'Content-Type':'application/json','authorization': logged_uuid}
    sendRequest('PATCH',url, data, {'Content-Type':'application/json'}, Callback.handler, 'add_courses',{}) 

def passedCourses():
    url = server + '/getPassedCourses'
    params = { "email": student_email} 
    headers = {'Content-Type':'application/json','authorization': logged_uuid}
    sendRequest('GET',url, params, {'Content-Type':'application/json'}, Callback.handler, 'get_passed_courses',{}) 

def readEmails():
    emails = []
    _file = open('students.json','r')
    for line in _file:
        emails.append(json.loads(line)['email'])
    _file.close()
    return emails

createUser()
login()
getStudent()
getThirties()
getOldies()
getStudentAdresses()
addCourses()
passedCourses()
for test, status in test_status_map.items():
    if status:
        print(colored("Test {0} succeeded".format(test), "green"))
    else:
        print(colored("Test {0} failed".format(test), "red"))
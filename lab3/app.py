from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from flask import Flask, request, jsonify, redirect
import json

# Connect to our local MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Choose InfoSys database
db = client['InfoSys']
students = db['Students']

# Initiate Flask App
app = Flask(__name__)

# Insert Student
# Create Operation
@app.route('/insertstudent', methods=['POST'])
def insert_student():
    # Request JSON data
    data = request.get_json()
    if "name" in data:
        name = data["name"]

    if "yearOfBirth" in data:
        yearOfBirth = data["yearOfBirth"]

    if "email" in data:
        email = data["email"]
    
    if students.find({"email":data["email"]}).count() == 0 :
        student = {"email": email, "name": name,  "yearOfBirth":yearOfBirth}
        # Add student to the 'students' collection
        students.insert_one(student)
        return {"name":student["name"], "msg":" was added to the MongoDB"}
    else:
        return {"msg":"A user with the given mail already exists"}


# Read Operations
# Get all students
@app.route('/getallstudents', methods=['GET'])
def get_all_students():
    iterable = students.find({})
    output = []
    for student in iterable:
         output.append(student)
    return str(output)

# Find student by email
@app.route('/getstudent/<string:email>', methods=['GET'])
def get_student_by_email(email):
    student = students.find_one({"email":email})
    student = {'_id':student["_id"],
            'name':student["name"],
            'email':student["email"], 
            'yearOfBirth':student["yearOfBirth"]}
    return str(student)
    # return jsonify({"student":student})

# Update Operation
# Find student by email and update
@app.route('/updatestudent/<string:email>', methods=['PUT'])
def update_student(email):
    student = students.find_one({"email":email})
    update_data = request.get_json()
    
@app.route('/deletestudent/<string:email>', methods=['DELETE'])
def delete_student(email):
    pass

# Run Flask App
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
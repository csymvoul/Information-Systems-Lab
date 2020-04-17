from pymongo import MongoClient
import json

# Connect to our local MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Choose InfoSys database
db = client['InfoSys']
students = db['Students']

def insert_student():
    student = {
        "name": "Chrysostomos Symvoulidis", 
        "email": "Symvoulidis", 
        "yearOfBirth": 1960, 
        "address": [{
            "street": "Karaoli kai Dimitriou 80", 
            "city": "Piraus", 
            "postcode": 12345
        }], 
        "gender": "male"
    }
    res = students.insert_one(student)

def get_all_students():
    iterable = students.find()
    for student in iterable:
        print(student)
    print("Total number of students: ", iterable.count())

def find_student(name):
    student = students.find_one({"name": name},
                                {"_id":0, "name": 1, "email":1})
    print(student)

def update_student():
    student = '''{
        "yearOfBirth": 1993, 
        "email": "simvoul@unipi.gr", 
        "address":[{
            "street": "Androutsou 150", 
            "city": "Piraeus", 
            "postcode": 18532
        }]
    }'''
    obj = json.loads(student)
    print(type(obj))
    
    # students.update_one({"email":"Symvoulidis"}, 
    #                     {
    #                         "$set":{
    #                             "email": obj["email"], 
    #                             "yearOfBirth": student["yearOfBirth"] #,
    #                             # "address.city": student["address][0]["city"]
    #                         }
    #                     })

update_student()

def delete_student():
    res = students.find_one_and_delete({"email": "Symvoulidis"})
    print(res)

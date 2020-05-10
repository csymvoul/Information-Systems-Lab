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
    print(res.inserted_id)

def get_all_students():
    # Find all students
    iterable = students.find()
    for student in iterable:
        print(student)

    # Print total count of students in the Students collection
    print("Total number of students: ", iterable.count())

def find_student(name):
    student = students.find_one({"name": name},
                                {"_id":0})
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

    student = json.loads(student)
    res = students.update_many({"email":"Symvoulidis"}, 
                        {
                            "$set":{
                                "email": student["email"], 
                                "yearOfBirth": student["yearOfBirth"], 
                                "address.0.city": student["address"][0]["city"],
                                "address.0.street": student["address"][0]["street"], 
                                "address.0.postcode": student["address"][0]["postcode"]
                            }
                        })
    print("Totally modified ", res.modified_count, " student")
    find_student("Chrysostomos Symvoulidis")

def delete_student():
    res = students.find_one_and_delete({"email": "simvoul@unipi.gr"})
    print("Deleted the student: ", res["_id"])

# insert_student()
# update_student()
# get_all_students()
find_student(name="Chrysostomos Symvoulidis")
# delete_student()
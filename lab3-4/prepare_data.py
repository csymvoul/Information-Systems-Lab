import json
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

# Choose InfoSys database
db = client['InfoSys']
students = db['Students']

def insert(entry):
    try:
        students.insert_one(entry)
        return True 
    except Exception as e:
        print(e)
        return False 

def main():
    file = open('students.json','r')
    lines = file.readlines()
    for line in lines:
        entry = None 
        try:
            entry = json.loads(line)
        except Exception as e:
            print(e)
            continue
        if entry != None:
            entry.pop("_id",None) 
            yb = entry["yearOfBirth"]["$numberInt"]
            if "address" in entry:
                address = entry["address"]
                n_address = []
                for adr in address:
                    postcode = adr["postcode"]["$numberInt"]
                    adr["postcode"] = postcode
                    n_address.append(adr)
                entry["address"] = n_address
            entry["yearOfBirth"] = int(yb) 
            if insert(entry):
                print("Document inserted")

main()
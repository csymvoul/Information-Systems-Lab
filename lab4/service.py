from flask import Flask, Response, request 
from pymongo import MongoClient
import time , json  

n_try = 10
db = None
app = Flask(__name__) 

def connect():
    global db 
    index = 0
    while index < n_try:
        client = MongoClient("localhost:27017")
        db = client["DS"]
        return db 

def insertDB(collection, data):
    global db 
    if db == None:
        raise ValueError("Db object is None")
    db[collection].insert_one(data)
    return True 

def getDB(collection, filter):
    global db  
    if db == None:
        raise ValueError("Db object is None")
    return db[collection].find(filter)


#endpoints 
@app.route('/insert-course', methods=['POST'])
def insert_course():
    data = None 
    try:
        data = json.loads(request.data)
    except Exception as e:
        print(e)
        return Response('Could not decode json content', status=400)
    
    required_fields = ['_id','name','ects']
    for item in required_fields:
        if not item in data:
            return Response(item+ ' item is missing', status=500)
    if insertDB(data):
        return Response('success', status=200)
    else:
        return Response('Internal error', status=500)

if __name__ == '__main__':
    connect()
    app.run('0.0.0.0', port=5000, debug=True)
    
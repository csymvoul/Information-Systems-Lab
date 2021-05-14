import json, requests 

student = {"email":"lab@unipi", "name":"John", "yearOfBirth": 1990}

url = "http://localhost:5000/insertstudent"

def sendRequest(data):
    try:
        response = requests.post(url=url, data=json.dumps(student))
        print(response.status_code)
        print(response.text)
    except Exception as e:
        print(e)
        print("An error occured")


sendRequest(student)


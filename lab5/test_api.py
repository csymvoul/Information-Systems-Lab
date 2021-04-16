import time, json, requests


class TestApi():
    def __init__(self):
        self.headers = {'content-type': 'application/json'}
        self.url = "http://localhost:5000"
        
    def insertStudent(self,name,year_of_birth,email):
        data = {'name': name, 'email': email, 'yearOfBirth': year_of_birth}
        try:
            response = requests.post(url=self.url+"/insertstudent",data=json.dumps(data), headers=self.headers)
            return response.text
        except Exception as e:
            print(e)
            return None 
        
    def getStudent(self,email):
        try:
            response = requests.get(url=self.url+"/getstudent/"+email, headers=self.headers)
            return response.json()
        except Exception as e:
            print(e)
            return None 

    def getAllStudents(self):
        try:
            response = requests.get(url=self.url+"/getallstudents",headers=self.headers)
            return response.text
        except Exception as e:
            print(e)
            return None 

    def updateStudent(self,email):
        try:
            response = requests.put(url=self.url+"/updatestudent/"+email,headers=self.headers)
            return response.text
        except Exception as e:
            print(e)
            return None 
    def deleteStudent(self,email):
        try:
            response = requests.delete(url=self.url+"/deletestudent/"+email,headers=self.headers)
            return response.text
        except Exception as e:
            print(e)
            return None 

def main():
    _students = [{'name':'student-1','email':'student-1@unipi.gr','yearOfBirth': 1998},{'name':'student-2','email':'student-2@unipi.gr','yearOfBirth': 1999}] 
    tester = TestApi()
    print("Inserting all students")
    for student in _students:
        resp = tester.insertStudent(student['name'],student['yearOfBirth'],student['email'])
        print(resp)
    print("getting all students")
    students = tester.getAllStudents()
    print(students)
    print("Update student year of birth")
    tester.updateStudent(_students[0]['email'])
    for student in _students:
        student_data = tester.getStudent(student['email'])
        print("----Single student-----")
        print(student_data)

    for student in _students:
        student_data = tester.deleteStudent(student['email'])
    students = tester.getAllStudents()
    print(students)  
    

if __name__=="__main__":
    main()
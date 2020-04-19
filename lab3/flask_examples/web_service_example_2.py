from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/getInfo", methods=['GET', 'POST'])
def get_info():
    if request.method =='GET':
        return {'response': 201, 'method': 'GET'}
    elif request.method == 'POST':
        data = json.loads(request.data)
        data['method']= 'POST'
        data['response']=201
        return data

if __name__ == '__main__':
    app.run(debug=True) 

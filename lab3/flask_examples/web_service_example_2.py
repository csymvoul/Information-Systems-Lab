from flask import Flask
from flask import request
import json

app = Flask(__name__)

@app.route("/getInfo")
def get_info():
    data = json.loads(request.data)
    return data

if __name__ == '__main__':
    app.run(debug=True) 
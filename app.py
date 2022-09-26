from flask import Flask
from flask import request
import json

app = Flask(name)

list_Json = {'id': 0, 'lat': 0.00000, 'lon': 0.00000}

@app.route("/")
def home():
    return json.dumps(list_Json)

@app.route("/routers", methods=['POST'])
def routers_post():
    global list_Json
    list_Json = json.loads(request.data)
    return json.dumps(list_Json)

@app.route("/routers", methods=['GET'])
def routers():
    return json.dumps(list_Json)

app.run(host="0.0.0.0")
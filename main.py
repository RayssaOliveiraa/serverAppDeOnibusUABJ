from flask import Flask, render_template
from flask import request
import json
from last_update import Lastupdate
from routers import Routers

app = Flask(__name__, template_folder='templates')

list_Json = {'id': 0, 'lat': 0.00000, 'lon': 0.00000}

@app.route("/")
def login():
  return render_template('login.html')

@app.route("/cadastro")
def cadastro():
  return render_template('cadastro.html')  

@app.route("/home")
def home():
    global list_Json
    busLocalization = Lastupdate.readLastUpdate()
    lastPoint = Lastupdate.readLastPoint()
    return render_template('index.html', lat=busLocalization['lat'], lon=busLocalization['lon'], last_point=lastPoint)

@app.route("/routers", methods=['POST'])
def routers_post():
    global list_Json
    list_Json = json.loads(request.data)
    ponto_de_parada = Routers().decodeRouter(list_Json)
    Lastupdate.saveLastUpdate(list_Json)
    Lastupdate.saveLastPoint(ponto_de_parada)
    return json.dumps(list_Json)

@app.route("/routers", methods=['GET'])
def routers():
    Routers()
    return json.dumps(list_Json)

app.run(host="0.0.0.0")
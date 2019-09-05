from flask import Flask
from flask import jsonify as json

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello_world():
  return json({"mensagem": "Hello World"})

from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify as json

app = Flask(__name__)
app.config.from_object('configuration')

db = SQLAlchemy(app)
marshmallow = Marshmallow(app)

from app.business import users

@app.route("/v1", methods=['GET'])
def hello_world():
  return json({"mensagem": "Hello World"})

@app.route('/v1/users', methods=['POST'])
def post_user():
  return users.post_user()

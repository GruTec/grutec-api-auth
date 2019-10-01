from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify as json
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config.from_object('configuration')
CORS(app, resources=r'/v1/*')

db = SQLAlchemy(app)
marshmallow = Marshmallow(app)

from app.business import users
from app.helpers import helpers

@app.route("/v1", methods=['GET'])
@cross_origin()
@helpers.token_required
def hello_world(current_user):
  return json({"mensagem": f'Hello {current_user}'})

@app.route('/v1/users', methods=['POST'])
@cross_origin()
def post_user():
  return users.post_user()

@app.route('/v1/users/<id>', methods=['PUT'])
@cross_origin()
@helpers.token_required
def update_user(id):
  return users.update_user(id)

@app.route('/v1/users', methods=['GET'])
@cross_origin()
@helpers.token_required
def get_users():
  return users.get_users()

@app.route('/v1/users/<id>', methods=['GET'])
@cross_origin()
@helpers.token_required
def get_user(id):
  return users.get_user(id)

@app.route('/v1/users/<id>', methods=['DELETE'])
@cross_origin()
@helpers.token_required
def delete_user(id):
  return users.delete_user(id)

@app.route('/auth', methods=['POST'])
@cross_origin()
def authenticate():
  return helpers.authenticate()

from werkzeug.security import generate_password_hash
from app.authentication import db
from flask import request
from flask import jsonify as json
from app.models.users import Users, user_schema, users_schema

def post_user():
  username = request.json['username']
  password = request.json['password']
  name = request.json['name']
  email = request.json['email']

  pass_hash = generate_password_hash(password)
  user = Users(username, pass_hash, name, email)

  try:
    db.create_all()
    db.session.add(user)
    db.session.commit()
    result = user_schema.dump(user)

    return json({'message': 'successfully registered', 'data': result}), 201
  except:
    return json({'message': 'unable to create', 'data': {}}), 500


def update_user(id):
  username = request.json['username']
  password = request.json['password']
  name = request.json['name']
  email = request.json['email']

  user = Users.query.get(id)

  if not user:
    return json({'message': 'user do not exist', 'data': {}}), 404

  password_hash = generate_password_hash(password)

  try:
    user.username = username
    user.password = password_hash
    user.name = name
    user.email = email

    db.session.commit()
    result = user_schema.dump(user)

    return json({'message': 'successfully updated', 'data': result}), 201
  except:
    return json({'message': 'unable to updated', 'data': {}}), 500


def get_users():

  users = Users.query.all()

  if users:
    result = users_schema.dump(users)

    return json({'message': 'successfully fetched', 'data': result})
  return json({'message': 'nothing found', 'data': {}})
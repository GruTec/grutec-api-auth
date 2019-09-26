import datetime
import jwt

from flask import request
from flask import jsonify as json
from functools import wraps
from app.business.users import get_user_by_username
from werkzeug.security import check_password_hash
from app.authentication import app

def authenticate():
  auth = request.authorization

  if not auth or not auth.username or not auth.password:
    return json({'message': 'could not verify', 'WWW-Authenticate': 'Basic auth="Login required"'}), 401

  user = get_user_by_username(auth.username)

  if not user:
    return json({'message': 'user not found', 'data': {}}), 401

  try:
    if user and check_password_hash(user.password, auth.password):
      jwt_token = jwt.encode({'username': user.username,
                              'exp': datetime.datetime.now() + datetime.timedelta(hours=12)},
                               app.config['SECRET_KEY'])

      return json({'message': 'validate successfully',
                   'token': jwt_token.decode('UTF-8'),
                   'exp': datetime.datetime.now() + datetime.timedelta(hours=12)})
  except:
    return json({'message': 'could not verify', 'WWW-Authenticate': 'Basic auth="Login required"'}), 401


def token_required(function):
  @wraps(function)
  def decorated(*args, **kwargs):
    token = request.args.get('token')

    if not token:
      return json({'message': 'token is missing', 'data': []}), 401

    try:
      data = jwt.decode(token, app.config.get('SECRET_KEY'), algorithms=['HS256'])
      current_user = get_user_by_username(user_username=data['username'])
    except:
      return json({'message': 'token is invalid or expired', 'data': []}), 401

    return function(current_user, *args, **kwargs)
  return decorated

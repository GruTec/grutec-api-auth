from app.authentication import app

DEBUG = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres@database/appdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

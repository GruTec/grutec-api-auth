from app.authentication import app

DEBUG = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres@database/appdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

SECRET_KEY = "$!bq8iakt)iq47ihmkz0k^@1w8fhutop2q8iakt)iq47ihmkz0kka4w6)!&t)iq47ihmkz0kka4dnhh0vim+"
from app.authentication import app
from app.authentication import db

db.init_app(app)

if __name__ == "__main__":
  app.run()
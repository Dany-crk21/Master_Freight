from Models.db import db
from datetime import datetime

class User(db.Model):
    __tablename__= "user"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone =  db.Column(db.Integer, unique=True, nullable=False)
    name = db.Column(db.String(120), nullable=False)
    car = db.Column(db.String(20), nullable=False)
    location = db.Column(db.String(120), nullable=False)

    def is_admin(self):
        return self.role == "admin"
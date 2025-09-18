from Models.db import db
from datetime import datetime

class User(db.Model):
    __tablename__= "user"

    id = db.column(db.Integer, primary_key=True)
    email = db.column(db.String(120), unique=True, nullable=False)
    phone =  db.column(db.int, unique=True, nullable=False)
    name = db.column(db.String(120), nullable=False)
    car = db.column(db.String(20), nullable=False)
    location = db.column(db.String(120), nullable=False)

    def is_admin(self):
        return self.role == "admin"
import uuid
from Models.db import db

class User(db.model):
    id = db.Column(db.String(36),primary_key = True, default = lambda: str(uuid.uuid4()))
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    password = db.Column(db.String(200), nullable = False)
    role = db.Column(db.String(20), default = "user") # possible roles: user, admin
    
    def to_dict(self):
        return{
            "id": self.id,
            "username":self.username,
            "email":self.email,
            "role":self.role
        }
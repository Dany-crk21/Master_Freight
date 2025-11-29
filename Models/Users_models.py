import uuid
from Models.db import db
from Models.SolicitudFlete import SolicitudFlete
from datetime import datetime

class User(db.Model):
    __tablename__= "users"
    
    id = db.Column(db.String(36),primary_key = True, default = lambda: str(uuid.uuid4()))
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    password = db.Column(db.String(64), nullable = False) # SHA -256 -> 64 hex chars
    salt = db.Column(db.String(32), nullable = False) # 16 bytes hex
    role = db.Column(db.String(20), default = "cliente") # possible roles: user, admin
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    imagen_perfil = db.Column(db.String(255), default="/static/imagen/default.png")
    
    solicitudes_cliente = db.relationship('SolicitudFlete',
                    foreign_keys='SolicitudFlete.cliente_id', 
                    back_populates='cliente',
                    lazy = True
                    )
    
    solicitudes_fletero = db.relationship('SolicitudFlete',
                    foreign_keys='SolicitudFlete.fletero_id',
                    back_populates='fletero',
                    lazy = True
                    )
    def __repr__(self):
        return f'<User {self.username}>'
    
    def to_dict(self):
        return{
            "id": self.id,
            "username":self.username,
            "email":self.email,
            "role":self.role,
            "imagen_perfil": self.imagen_perfil,
            }
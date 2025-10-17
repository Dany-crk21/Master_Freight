from Models.db import db

class Fletero(db.Model):
    __tablename__ = 'fletero'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    telefono = db.Column(db.String(50), nullable=True)
    vehiculo = db.Column(db.String(100), nullable=True)

    # Relación inversa: un fletero puede tener varias solicitudes asignadas
    solicitudes = db.relationship('SolicitudFlete', back_populates='fletero', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'email': self.email,
            'telefono': self.telefono,
            'vehiculo': self.vehiculo
        }
    


     
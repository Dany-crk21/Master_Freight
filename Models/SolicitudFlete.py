from Models.db import db
from datetime import datetime

class SolicitudFlete(db.Model):
    __tablename__='solicitudFletes'
    
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)
    estado = db.Column(db.String(50), default= 'pendiente')
    origen = db.Column(db.String(100))
    destino = db.Column(db.String(100))
    detalle = db.Column(db.String(200))
    
    #Foreign keys
    cliente_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    fletero_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=True)

    cliente = db.relationship('User', foreign_Keys=[cliente_id], back_populates='solicitudes')
    fletero = db.relationship('User', foreign_keys=[fletero_id])
    
    def to_dict(self):
        return{
            'id': self.id,
            'fecha': self.fecha,
            'estado': self.estado,
            'origen': self.origen,
            'destino': self.destino,
            'detalle': self.detalle,
            'cliente_id': self.cliente_id,
            'fletero_id': self.fletero_id
            }
         
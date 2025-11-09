from Models.db import db
from datetime import datetime

class SolicitudFlete(db.Model):
    __tablename__='solicitud_Fletes'
    
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)
    estado = db.Column(db.String(50), default= 'pendiente')
    origen = db.Column(db.String(100))
    destino = db.Column(db.String(100))
    detalle = db.Column(db.String(200))
    
    #Relaciones con usuarios cliente y fletero
    cliente_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    fletero_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=True)

    cliente = db.relationship('User', foreign_keys=[cliente_id], back_populates='solicitudes_cliente')
    fletero = db.relationship('User', foreign_keys=[fletero_id], back_populates='solicitudes_fletero')
    
    def to_dict(self):
        return{
            'id': self.id,
            'fecha': self.fecha.isoformat(),
            'estado': self.estado,
            'origen': self.origen,
            'destino': self.destino,
            'detalle': self.detalle,
            'cliente_id': self.cliente_id,
            'fletero_id': self.fletero_id
        }
         
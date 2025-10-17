from Models.db import db
from datetime import datetime

class solicitudFlete(db.Model):
    __tablename__='solicitudFlete'
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)
    estado = db.Column(db.String(50), default= 'pendiente')
    origen = db.Column(db.String(100))
    destino = db.Column(db.String(100))
    detalle = db.Column(db.String(200))
    
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False)
    fletero_id = db.Column(db.Integer, db.ForeignKey('fletero.id'), nullable=True)

    cliente = db.relationship('clientes', foreign_keys=[cliente_id], back_populates='solicitudes')
    fletero = db.relationship('fletero', foreign_keys=[fletero_id], back_populates='solicitudes')
    
    def to_dict(self):
        return{
            'id': self.id,
            'fecha': self.fecha,
            'estado': self.estado,
            'origen': self.origen,
            'destino': self.destino,
            'detalle': self.detalle,
            'cliente_id': self.cliente_id,
            'fletero_id': self.fletero_id}
         
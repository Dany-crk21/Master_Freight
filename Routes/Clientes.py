from flask import Blueprint, request, jsonify
from Models.SolicitudFlete import solicitudFlete
from Models.db import db
from datetime import datetime

Clientes_bp = Blueprint('clientes', __name__)
# Rutas para clientes
@Clientes_bp.route('/cliente/solicitar', methods=['post'])
def solicitar_flete():
    data = request.get.json()
    nueva_solicitud = solicitudFlete(
        origen=data['origen'],
        destino=data['destino'],
        detalle=data['detalle'],
        cliente_id=data['cliente_id']
    )
    db.session.add(nueva_solicitud)
    db.session.commit()
    return jsonify({'message':'solicitud creada exitosamente'}), 201

# Ver solicitudes del cliente
@Clientes_bp.route('/cleinte/<int:cliente_id>/solicitudes', methods=['GET'])
def ver_solicitudes(cliente_id):
    solicitudes = solicitudFlete.query.filter_by(cliente_id=cliente_id).all()
    result = [{
        'id': s.id,
        'fecha': s.fecha,
        'estado': s.estado,
        'origen': s.origen,
        'destino': s.destino,
        'detalle': s.detalle,    }for s in solicitudes]
    return jsonify(result), 200
                   
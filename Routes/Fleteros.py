from flask import Blueprint, request, jsonify
from Models.SolicitudFlete import solicitudFlete
from Models.db import db
from datetime import datetime

Fleteros_bp = Blueprint('fleteros', __name__)

# Ver solicitudes asignadas al fletero
@Fleteros_bp.route('/fletero/<int:fletero_id>/solicitudes', methods=['GET'])
def ver_solicitudes(fletero_id):
    solicitudes = solicitudFlete.query.filter_by(estado='pendiente').all()
    result = [{
        'id': s.id,
        'fecha': s.fecha,
        'estado': s.estado,
        'origen': s.origen,
        'destino': s.destino,
        'detalle': s.detalle,
        'fecha': s.fecha,
    }for s in solicitudes]
    return jsonify(result)

# Aceptar o Rechazar solicitud
@Fleteros_bp.route('/fletero/responder', methods=['PUT'])
def responder_solicitud():
    data = request.get_json()
    solicitud = solicitudFlete.query.get(data['solicitud_id'])
    if not solicitud:
        return jsonify({'error': 'Solicitud no encontrada'}), 404
    
    solicitud.estado = data['estado'] # 'aceptada' o 'rechazada'
    solicitud.fletero_id = data['fletero_id']
    db.session.commit()
    return jsonify({"message": f"solicitud{data['estado']} correctamente"}), 200


from flask import Blueprint, request, jsonify
from Models.SolicitudFlete import SolicitudFlete
from Models.db import db
from Utils.security import token_required

Fleteros_bp = Blueprint('fleteros', __name__)

# Ver solicitudes asignadas al fletero
@Fleteros_bp.route('/fletero/solicitudes', methods=['GET'])
@token_required(role='fletero')
def ver_solicitudes(current_user):
    solicitudes = SolicitudFlete.query.filter_by(estado='pendiente',fletero_id=None).all()
    
    if not solicitudes:
        return jsonify({'message':'No hay solicitudes disponibles'}), 200
    result = [{
        'id': s.id,
        'fecha': s.fecha.isoformat(),
        'estado': s.estado,
        'origen': s.origen,
        'destino': s.destino,
        'detalle': s.detalle,
        'fecha': s.fecha,
    } for s in solicitudes]
    return jsonify(result), 200

# Aceptar o Rechazar solicitud
@Fleteros_bp.route('/fletero/responder', methods=['PUT'])
@token_required(role='fletero')
def responder_solicitud(current_user):
    data = request.get_json()
    solicitud = SolicitudFlete.query.get(data['solicitud_id'])
    if not solicitud:
        return jsonify({'error': 'Solicitud no encontrada'}), 404
    
    solicitud.estado = data['estado'] # 'aceptada' o 'rechazada'
    solicitud.fletero_id = current_user.id
    db.session.commit()
    return jsonify({"message": f"solicitud{data['estado']} correctamente"}), 200
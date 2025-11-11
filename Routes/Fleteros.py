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
        'origen': s.origen,
        'destino': s.destino,
        'detalle': s.detalle,
        'origen_lat': s.origen_lat,
        'origen_lng': s.origen_lng,
        'destino_lat': s.origen_lat,
        'destino_lng': s.origen_lng,
        'estado': s.estado,
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

# Aceptar una solicitud
@Fleteros_bp.route('/fletero/completar/<int:id>', methods=['POST'])
@token_required(role='fletero')
def completar_solicitud(current_user, id):
    solicitud = SolicitudFlete.query.get(id)

    if not solicitud or not solicitud.fletero_id != current_user.id:
        return jsonify({'message': 'Solicitud no encontrada o no asignada a ti'}), 403
    
    solicitud.estado = 'aceptada'
    solicitud.fletero_id = current_user.id
    db.session.commit()

    return jsonify({'message': 'Solicitud aceptada'})

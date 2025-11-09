from flask import Blueprint, request, jsonify
from Models.SolicitudFlete import SolicitudFlete
from Models.db import db
from Routes.Users import token_required

Clientes_bp = Blueprint('clientes', __name__)

# Rutas para clientes
@Clientes_bp.route('/cliente/solicitar', methods=['POST'])
@token_required(role='cliente')
def solicitar_flete(current_user):
    data = request.get_json()
    
    required_fields = ['origen', 'destino', 'detalle']
    if not data or not all(field in data for field in required_fields):
        return jsonify({'error': 'faltan campos requeridos'}), 400
    nueva_solicitud = SolicitudFlete(
        origen=data['origen'],
        destino=data['destino'],
        detalle=data['detalle'],
        cliente_id=current_user.id
    )
    db.session.add(nueva_solicitud)
    db.session.commit()
    return jsonify({'message':'solicitud creada exitosamente'}), 201

# Ver solicitudes del cliente
@Clientes_bp.route('/cliente/solicitudes', methods=['GET'])
@token_required(role='cliente')
def ver_solicitudes(current_user):
    solicitudes = SolicitudFlete.query.filter_by(cliente_id=current_user.id)\
        .order_by (SolicitudFlete.fecha.des()).all()
        
    if not solicitudes:
            return jsonify({'message':'No tienes solicitudes registradas'}), 200
    
    result = [{
        'id': s.id,
        'fecha': s.fecha if s.fecha else None,
        'estado': s.estado,
        'origen': s.origen,
        'destino': s.destino,
        'detalle': s.detalle,    
    } for s in solicitudes]

    return jsonify(result), 200
                   
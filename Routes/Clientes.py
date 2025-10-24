from flask import Blueprint, request, jsonify
from Models.SolicitudFlete import SolicitudFlete
from Models.Users_models import User
from Models.db import db
from Utils.security import token_required
Clientes_bp = Blueprint('clientes', __name__)

# Rutas para clientes
@Clientes_bp.route('/cliente/solicitar', methods=['POST'])
@token_required(role='cliente')
def solicitar_flete(current_user):
    data = request.get_json()
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
    solicitudes = SolicitudFlete.query.filter_by(cliente_id=current_user.id).all()
    result = [{
        'id': s.id,
        'fecha': s.fecha,
        'estado': s.estado,
        'origen': s.origen,
        'destino': s.destino,
        'detalle': s.detalle,    }for s in solicitudes]
    return jsonify(result), 200
                   
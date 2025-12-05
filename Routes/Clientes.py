from flask import Blueprint, request, jsonify,render_template
from Models.SolicitudFlete import SolicitudFlete
from Models.db import db
from Utils.security import token_required

Clientes_bp = Blueprint('clientes', __name__)

# Panel del Cliennte
@Clientes_bp.route('/cliente/panel', methods=['GET'])
def cliente_panel():
    return render_template('Panel_Cliente.html')

# Obtener nombre y rol del cliente
@Clientes_bp.route('/cliente/me', methods=['GET'])
@token_required(role='cliente')
def cliente_me(current_user):
    return jsonify({
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email,
        "role": current_user.role,
        "imagen_perfil": current_user.imagen_perfil
    }), 200

        
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
        .order_by (SolicitudFlete.fecha.desc()).all()
        
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
                   
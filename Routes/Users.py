from flask import Blueprint, request, jsonify, render_template
from Models.Users_models import User
from Models.db import db
from Utils.security import make_password_hash, check_password,token_required
import jwt
from flask import current_app as app
from datetime import datetime, timedelta

auth_bp = Blueprint('auth',__name__)

@auth_bp.route('/register/cliente', methods=['GET','POST'])
def register_cliente():
    return register_with_role('cliente')

@auth_bp.route('/register/fletero', methods=['POST'])
def register_fletero():
    return register_with_role('fletero')

def register_with_role(role):
    data = request.get_json()
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'message':'Email already exists'}), 400
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'message':'Username already exists'}), 400
    hash_hex, salt_hex = make_password_hash(data['password'])
    new_user = User(
        username=data['username'],
        email=data['email'],
        password = hash_hex,
        salt = salt_hex,
        role = role
    ) 
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message':f'{role} created successfully'}),201

@auth_bp.route('login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('/auth/login.html')
    data = request.get_json()
    user = User.query.filter_by(email=data["email"]).first()
    if not user or not check_password(data["password"], user.password, user.salt):
        return jsonify({"message": "invalid credentials"}), 401
    
    token = jwt.encode({
        'id': user.id,
        'exp': datetime.utcnow() + timedelta(hours=1)
    }, app.config['SECRET_KEY'], algorithm="HS256")
     
    # Aqui agregamos username ademas de token y role
    return jsonify({
        "token": token,
        'role': user.role,
        'username': user.username
    }), 200

    
# panel de usuario autenticado
@auth_bp.route("/dashboard", methods=["GET"])
@token_required()
def dashboard_page(current_user):
    if current_user.role == 'cliente':
        return render_template("cliente_dashboard.html")
    elif current_user.role == 'fletero':
        return render_template("fletero_dasboard.html")
    else:
        return "adimin_dasboard.html"

@auth_bp.route("/api/dashboard", methods=["GET"])
@token_required()
def dashboard_api(current_user):
    return jsonify({
        "username": current_user.username,
        'role': current_user.role
    })

@auth_bp.route("/api/users", methods=["GET"])
@token_required(role='admin') # solo admin puede acceder
def list_users(current_user):
    users = User.query.all()
    users_data = [
        {
            "id": u.id,
            "username": u.username,
            "email": u.email,
            "role": u.role
        } for u in users
    ]
    return jsonify(users_data)
    
from flask import Blueprint, request, jsonify, render_template
from Models.Users_models import User
from Models.db import db
from Utils.security import make_password_hash, check_password
import jwt
from flask import current_app as app
from functools import wraps
from datetime import datetime, timedelta

auth_bp = Blueprint('auth',__name__)

def token_required(role=None):
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
                token = request.headers.get('Authorization')
                if not token:
                    return jsonify({"message":"Token is missing!"}), 401
                try:
                    token = token.split()[1] # Bearer <token>
                    data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
                    current_user = User.query.get(data['id'])
                    if not current_user:
                        return jsonify({"message":"User not found"}), 404
                    if role and current_user.role != role:
                        return jsonify({"message":"Unauthorized access"}), 403
                except Exception as e:
                    return jsonify({"message":"Token is invalid!",'error':str(e)}), 401
                return f(current_user, *args, **kwargs)
        return decorated
    return decorator


@auth_bp.route('/register/cliente', methods=['POST'])
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
    return jsonify({'message':'User created successfully'}),201

@auth_bp.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
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
    return render_template("cliente_dashboard.html")

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
    
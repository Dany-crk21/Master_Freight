from flask import Blueprint, request, jsonify, render_template
from models.users_models import User
from models.db import db
from werkzeug.security import generate_password_hash, check_password_hash
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
                    
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if User.query.filter_by(email=data['email']).first():
        return jsonify({"message":"Email already exists"}), 400
    hashed_password = generate_password_hash(data['password'])
    new_user = User(
        username=data['username'],
        email=data['email'],
        password= hashed_password,
        role=data.get('role','user') # por defecto es 'user'
    )     
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message":"User created sucessfully"}), 201
   
    
@auth_bp.route("/register", methods=["GET"])
def register_page():
    return render_template("register.html")


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data["email"]).first()
    if not user or not check_password_hash(user.password, data["password"]):
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

@auth_bp.route("/login", methods=["GET"])
def login_page():
    return render_template("login.html")
    
@auth_bp.route("/dashboard", methods=["GET"])
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
    
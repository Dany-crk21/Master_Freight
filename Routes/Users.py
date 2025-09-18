from flask import Blueprint, request, jsonify, render_template
from Models.Users_models import User
from Models.db import db
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
                    token = token.split(" ")[1] # Bearer <token>
                    data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
                    current_user = User.query.get(data['id'])
                    if not current_user:
                        return jsonify({"message":"User not found"}), 404
                    if role and current_user.role != role:
                        return jsonify({"message":"Unauthorized access"}), 403
                except Exception as e:
                    return jsonify({"message":"Token is invalid!",'error':str(e)},), 401
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
        password= hashed_pw,
        role=data.get('role','user') # por defecto es 'user'
    )     
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message":"User created sucessfully"}), 201
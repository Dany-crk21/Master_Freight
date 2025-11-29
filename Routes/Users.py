from flask import Blueprint, request, jsonify, render_template
from Models.Users_models import User
from Models.db import db
from Utils.security import make_password_hash, check_password, token_required
from werkzeug.utils import secure_filename
import os
import jwt
from flask import current_app as app
from datetime import datetime, timedelta

auth_bp = Blueprint('auth', __name__)

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
        role = role,
        imagen_perfil = "/static/default_profile.png"
    ) 
    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        'message':f'{role} created successfully'}), 201

@auth_bp.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('auth/login.html')
    data = request.get_json()
    print(data)
    user = User.query.filter_by(email=data["email"]).first()
    print(user)
    if not user or not check_password(data["password"], user.password, user.salt):
        return jsonify({"message": "invalid credentials"}), 401
    
    token = jwt.encode({
        'id': user.id,
        'exp': datetime.utcnow() + timedelta(hours=1)
    }, app.config['SECRET_KEY'], algorithm="HS256")
    print(token)
    print('role:', user.role)
     
    # Aqui agregamos username ademas de token y role
    return jsonify({
        "success": True,
        "message": "Login succesful",
        "token": token,
        'role': user.role,
        'username': user.username
    }), 200
    
   # Ruta de Registro
@auth_bp.route("/register", methods=["GET"])
def show_register_page():
    return render_template("auth/register.html")

  
# Servir template de dashboard
@auth_bp.route("/dashboard", methods=["GET"])
def dashboard_page():
    return render_template('dashboard.html')

# Panel de usuario autenticado
@auth_bp.route("/api/dashboard", methods=["GET"])
@token_required()
def dashboard_api(current_user):
    return jsonify({
        'id': current_user.id,
        'username': current_user.username,
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

# Ruta para subir imagen de perfil
UPLOAD_FOLDER = 'static/uploads/profile_pics'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
def allowed_file(filename):
    return "." in filename and \
            filename.rsplit(".",1)[1].lower() in ALLOWED_EXTENSIONS
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER   
    
@auth_bp.route("/upload_profile", methods=['POST'])
@token_required()
def upload_profile_picture(current_user):
    if 'imagen' not in request.files:
        return jsonify({'message':"No file part"}), 400
    
    file = request.files["imagen"]
    
    if file.filename == "":
        return jsonify({'message':"No selected file"}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(current_user.id + "_" + file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Guardar la ruta en la BD
        current_user.profile_image = filename
        db.session.commit()
        
        return jsonify({
            "message":"Imagen subida exitosamente",
            "Imagen_perfil": current_user.imagen_perfil
        }), 200
    
    
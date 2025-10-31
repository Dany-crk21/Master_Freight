import os
import hashlib
import jwt
<<<<<<< HEAD
from flask import request, jsonify, current_app as app
from functools import wraps
from Models.Users_models import User
=======
from functools import wraps
from flask import request, jsonify
from Models.Users_models import User
from flask import current_app as app
>>>>>>> 99a96ac9975686b435f7b7b228387f7adc72f611

#sha-256
def _sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def make_password_hash(password:str) -> tuple[str,str]:
    salt = os.urandom(16) # 16 bytes
    salt_hex = salt.hex()
    hash_hex = _sha256_hex(salt + password.encode('utf-8'))
    return hash_hex, salt_hex

def check_password(password: str, hash_hex: str, salt_hex: str) -> bool:
    salt = bytes.fromhex(salt_hex)
    return _sha256_hex(salt + password.encode('utf-8')) == hash_hex
<<<<<<< HEAD
    
=======

>>>>>>> 99a96ac9975686b435f7b7b228387f7adc72f611
def token_required(role=None):
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
                token = request.headers.get('Authorization')
                if not token:
                    return jsonify({"message":"Token is missing!"}), 401
                try:
                    token = token.split()[1] # Bearer <token>
<<<<<<< HEAD
                    data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
                    current_user = User.query.get(data['id'])
=======
                    data = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
                    current_user = User.query.get(data["id"])
>>>>>>> 99a96ac9975686b435f7b7b228387f7adc72f611
                    if not current_user:
                        return jsonify({"message":"User not found"}), 404
                    if role and current_user.role != role:
                        return jsonify({"message":"Unauthorized access"}), 403
                except Exception as e:
                    return jsonify({"message":"Token is invalid!",'error':str(e)}), 401
                return f(current_user, *args, **kwargs)
        return decorated
    return decorator
<<<<<<< HEAD
                    

            
=======
                
                        
        

    
>>>>>>> 99a96ac9975686b435f7b7b228387f7adc72f611

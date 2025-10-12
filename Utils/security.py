import os
import hashlib

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
    
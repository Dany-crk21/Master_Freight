from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("JWT_SECRET", "SUPERSECRET")
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@{os.getenv('MYSQL_HOST')}:{os.getenv('MYSQL_PORT', '3306')}/{os.getenv('MYSQL_DATABASE')}"
    
SQLALCHEMY_TRACK_MODIFICATIONS = False
from flask import Flask, render_template
from Config import config
from Models.db import db
from Routes.Users import auth_bp
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(config)
app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app,db)
app.register_blueprint(auth_bp)

from Routes.Users import auth_bp

with app.app_context():
    db.create_all()  

if __name__ == "__main__":
    app.run(debug=True)
    
    
    
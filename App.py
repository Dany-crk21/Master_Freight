from flask import Flask, render_template, redirect, url_for
from Config import config
from Models.db import db
from Routes.Users import auth_bp
from Routes.Clientes import Clientes_bp
from Routes.Fleteros import Fleteros_bp
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(config)
app.config['secret_key'] = config.SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app,db)
# Registro de Rutas
app.register_blueprint(auth_bp)
app.register_blueprint(Clientes_bp)
app.register_blueprint(Fleteros_bp)


@app.route('/')
def home():
    # return redirect(url_for('auth.login'))
    return render_template('mapa.html')

with app.app_context():
    db.create_all()  

if __name__ == "__main__":
    app.run(debug=True)
    
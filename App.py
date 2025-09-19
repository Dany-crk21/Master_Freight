from flask import Flask, render_template
from Config import config
from Models.db import db
from Routes.Users import auth_bp
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(config)


db.init_app(app)
migrate = Migrate(app,db)
app.register_blueprint(auth_bp)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    
    
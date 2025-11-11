from flask import Blueprint,render_template
from Models.db import db
from Utils.security import token_required
from flask import current_app as app

main_bp = Blueprint('main', __name__)
@main_bp.route('/home', methods=['GET'])
@token_required
def home(current_user):
    return render_template('home.html', user=current_user)

@main_bp.route('/nosotros', methods=['GET'])
@token_required
def nosotros_page(current_user):
    return render_template('nosotros.html', user=current_user)

@main_bp.route('/contacto', methods=['GET'])
@token_required
def contacto_page(current_user):
    return render_template('contacto.html', user=current_user)

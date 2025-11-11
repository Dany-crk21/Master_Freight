from flask import Blueprint, render_template
from Utils.security import token_required

from flask import Blueprint, render_template
from Models.db import db
from Utils.security import token_required

main_bp = Blueprint('main', __name__)

@main_bp.route('/home', endpoint='home_page', methods=['GET'])
@token_required()
def home(current_user):
    return render_template('home.html', user=current_user)

@main_bp.route('/nosotros', endpoint='nosotros_page', methods=['GET'])
@token_required()
def nosotros(current_user):
    return render_template('nosotros.html', user=current_user)

@main_bp.route('/contacto', endpoint='contacto_page', methods=['GET'])
@token_required()
def contacto(current_user):
    return render_template('contacto.html', user=current_user)

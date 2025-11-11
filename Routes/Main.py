from flask import Blueprint, render_template
from Utils.security import token_required

main_bp = Blueprint('main', __name__)

@main_bp.route('/home', methods=['GET'])
def home():
    return render_template('home.html')

@main_bp.route('/nosotros', methods=['GET'])
def nosotros_page():
    return render_template('nosotros.html')

@main_bp.route('/contacto', methods=['GET'])
def contacto_page():
    return render_template('contacto.html')

@main_bp.route('/reserva', methods=['GET'])
def reserva_page():
    return render_template('reserva.html')

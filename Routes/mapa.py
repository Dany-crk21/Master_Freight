from flask import Blueprint, request, jsonify, render_template
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from Utils.security import token_required
from Models.Users_models import User

map_bp = Blueprint('map', __name__)

# Recibe una dirección y devuelve coordenadas (lat, lng).
map_bp.route('/maps/geocode')
def geocode(lat, lng):
    pass

# Devuelve distancia, tiempo y puntos de la ruta.
map_bp.route('/maps/directions')
def direction():
    pass

# Mostrar el mapa mediante HTML.
map_bp.route('/map')
def get_map():
    pass
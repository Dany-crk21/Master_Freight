from flask import Blueprint
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
const map = L.map('map').setView([51.505, -0.09], 13);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

/* https://maps.wikimedia.org/osm-intl/{{z}/{x}/{y}.png */

// Intentar centrar en la ubicación del usuario
map.locate({ setView: True, maxZoom: 16 });
map.on('locationfound', (e) => {
    L.marker(e.Latlng).addTo(map).bindPopup('Estas aca').openPopup();
});

let origen = null;
let destino = null;
let controlRuta = null; // para almacenar la ruta actual

// Función para trazar la ruta entre origen y destino
function trazarRuta(origen, destino) {

  // Si ya hay una ruta trazada, eliminarla antes de dibujar una nueva
    if (controlRuta) {
        map.removeControl(controlRuta);
    }

    controlRuta = L.Routing.control({
        waypoints: [
            L.latLng(origen.lat, origen.lng),
            L.latLng(destino.lat, destino.lng)
        ],
        routeWhileDragging: true,
        showAlternatives: false,
        lineOptions: {
            styles: [{ color: 'blue', opacity: 0.7, weight: 5 }]
        },
        createMarker: function() { return null; } // 
    }).addTo(map);
}

// Función que selecciona puntos al hacer clic
function seleccionarPunto(e) {
    if (!origen) {
        origen = e.latlng;
        L.marker(origen).addTo(map).bindPopup('Origen').openPopup();
    } else if (!destino) {
        destino = e.latlng;
        L.marker(destino).addTo(map).bindPopup('Destino').openPopup();
        trazarRuta(origen, destino);
    } else {
    // Si ya hay dos puntos, reinicia la selección
        map.eachLayer(layer => {
        if (layer instanceof L.Marker && !(layer instanceof L.TileLayer)) {
            map.removeLayer(layer);
        }
    });
    origen = e.latlng;
    destino = null;
    if (controlRuta) {
        map.removeControl(controlRuta);
    }
    L.marker(origen).addTo(map).bindPopup('Nuevo Origen').openPopup();
  }
}

// Escuchar clics en el mapa
map.on('click', seleccionarPunto);
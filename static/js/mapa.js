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
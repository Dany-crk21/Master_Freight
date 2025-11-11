export function renderFleteroDashboard(container) {
    container.innerHTML = `
    <div class="card shadow-sm p-4">
        <h3 class="text-center mb-3 text-primary">Panel del Fletero</h3>
        <p class="text-muted mb-3 text-center">Visualiza las solicitudes de flete en el mapa.</p>

        <div id="map" style="height: 500px;" class="rounded border"></div>
        <div id="solicitudesList" class="list-group"></div>
    </div>
    `;

    const token = localStorage.getItem('token')
    const map = L.map('map').setView([-32.889, -68.845], 13); // Mendoza por defecto

    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; OpenStreetMap contributors'
    }).addTo(map);

    const list = document.getElementById('solicitudesList');

    // Cargar solicitudes
    async function loadSolicitudes() {
        list.innerHTML = '<p class="text-center text-muted">Cargando...</p>';
        
        const res = await fetch('/fletero/solicitudes', {
            headers: { 'Authorization': `Bearer ${token}` }
        });
        const data = await res.json();
        list.innerHTML = '';

        if (!data.length) {
            list.innerHTML = '<p class="text-muted text-center">No hay solicitudes pendientes.</p>'
            return;
        }

        data.forEach(s => {
            const item = document.createElement('div');
            item.className = 'list-group-item';
            item.innerHTML = `
                <strong>${s.origen}</strong> => ${s.destino}<br>
                <small>${s.detalle || ''}</small><br>
                <button class="btn btn-primary btn-sm mt-2">Aceptar</button>
            `;
            item.querySelector('button').addEventListener('click', () => aceptarSolicitud(s.id));
            list.appendChild(item);
        });
        
            // Dibujar en mapa
            if (s.origen_lat && s.destino_lat) {
                const origen = [s.origen_lat, s.origen_lng];
                const destino = [s.destino_lat, s.destino_lng];

            L.marker(origen).addTo(map).bindPopup(`Origen - ${s.origen}`);
            L.marker(destino).addTo(map).bindPopup(`Destino - ${s.destino}`);

            fetch(`/maps/directions?origen_lat=${origen[0]}&origen_lng=${origen[1]}&destino_lat=${destino[0]}&destino_lng=${destino[1]}`)
                    .then(res => res.json())
                    .then(ruta => {
                        if (ruta.coordenadas) {
                            const coords = ruta.coordenadas.map(([lng, lat]) => [lat, lng]);
                            L.polyline(coords, { color: 'blue' }).addTo(map);
                        }
                    });
            }
        }

    // Aceptar solicitud 
    async function aceptarSolicitud(id) {
        const res = await fetch(`/fletero/completar/${id}`, {
            method: 'POST',
            headers: { 'Authorization': `Bearer ${token}`}
        });
        const data = await res.json();
        alert(data.message);
        loadSolicitudes();
    }
    loadSolicitudes();
}   

    


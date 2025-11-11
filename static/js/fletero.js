export function renderFleteroDashboard(container) {
    container.innerHTML = `
    <div class="card shadow-sm p-4">
        <h3 class="text-center mb-3 text-primary">Panel del Fletero</h3>
        <p class="text-muted mb-3 text-center">Visualiza las solicitudes de flete en el mapa.</p>

        <div id=map style="height: 500px;" class="rounded border"></div>
    </div>
    `;

    // Cargar mapa con leaflet 
    const map = L.map('map').setView([-32.889, -68.845], 13); // Mendoza por defecto

    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; OpenStreetMap contributors'
    }).addTo(map);

    // Aquí podrías hacer fetch a tus solicitudes activas
    // y mostrar marcadores con las rutas
    /*
    fetch('/fletero/solicitudes', { headers: { 'Authorization': `Bearer ${token}` }})
        .then(res => res.json())
        .then(data => { ... })
    */
}
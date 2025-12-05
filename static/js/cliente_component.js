export function renderClienteDashboard(container) {

    container.innerHTML = `
        <div class="cliente-panel">

            <h2 class="text-center mt-3">Bienvenido Cliente</h2>

            <form id="solicitudForm" class="card p-3 shadow mb-4">
                <h5> Crear una Solicitud </h5>
                <div class="mb-3">
                    <label class="form-label">Origen</label>
                    <input type="text" class="form-control" id="origen" required>
                </div>
                <div class="mb-3">
                    <label class="form-label">Destino</label>
                    <input type="text" class="form-control" id="destino" required>
                </div>
                
                <div class="mb-3">
                    <label class="form-label">Detalle</label>
                    <textarea class="form-control" id="detalle" rows="3"></textarea>
                </div>
                <button type="submit" class="btn btn-success w-100">Solicitar Flete</button>
            </form>

            <h4 class="text-secondary mb-3">Mis solicitudes</h4>
            <div id="solicitudes" class="list-group"></div>
        </div> 
    `;

    const token = localStorage.getItem('token');
    const form = document.getElementById('solicitudForm');
    const list = document.getElementById('solicitudes');

    // Crear Solicitud
    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const data = {
            origen: e.target.origen.value,
            destino: e.target.destino.value,
            detalle: e.target.detalle.value
        };

        const res = await fetch('/cliente/solicitar', {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${token}`
            },
            body: JSON.stringify(data)
        });

        const result = await res.json();
        alert(result.message || "Solicitud enviada con éxito");
        loadSolicitudes();
    });

    // obtener solicitudes
    async function loadSolicitudes() {
        const res = await fetch('/cliente/solicitudes', {
            headers: { 'Authorization': `Bearer ${token}` }
        });

        const data = await res.json();
        list.innerHTML = '';

        if (!data.length === 0 || data.message) {
            list.innerHTML =  `<p class="text-muted">No tienes solicitudes registradas.</p>`;
            return;
        }

        data.forEach(s => {
            const item = document.createElement('div');
            item.className = "list-group-item shadow-sm";
            item.innerHTML = `
                <strong>${s.origen}</strong> → ${s.destino}<br>
                <small> Estado: ${s.estado}</small> | <small>${s.fecha || ""}</small><br>
                <em>${s.detalle}</em>
            `;
            list.appendChild(item);
        });
    }

    loadSolicitudes();
}
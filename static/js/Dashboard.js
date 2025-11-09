document.addEventListener('DOMContentLoaded', async (e) => {
    const role = localStorage.getItem('role');
    const username = localStorage.getItem('username');
    const token = localStorage.getItem('token');

    if (!role || !token) {
        window.location.href = '/login';
        return;
    }

    const navbar = document.getElementById('navbar');
    const content = document.getElementById('content');

    navbar.innerHTML = `
    <h2>Bienvenido, ${username}</h2>
    <button id='logoutBtn'>Cerrar sesión</button>
    `;

    document.getElementById('logoutBtn').addEventListener('click', () => {
        localStorage.clear();
        window.location.href = '/login';
    });

    try {
        const res = await  fetch('/api/dashboard', {
            headers: { 
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json'
            }
        });

        if (!res.ok) {
            const data = await res.json();
            alert(data.message || 'Token invalido');
            localStorage.clear();
            window.location.href = '/login'
            return;
        }

        const data = await res.json();
        console.log('Datos validos:', data);

        // Cargar dashboard según el rol.
        if (role === 'admin') {
            import('/static/js/admin.js').then(module => module.renderAdminDashboard(content));
        } else if (role === 'fletero') {
            import('/static/js/fletero.js').then(module => module.renderFleteroDashboard(content));
        }
        else {
            import('/static/js/cliente.js').then(module => module.renderClienteDashboard(content));
        }

    } catch (err) {
        console.log('Error al validar token', err);
        localStorage.clear();
        window.location.href = '/login';
    }
});
document.addEventListener('DOMContentLoaded', async (e) => {
    const role = localStorage.getItem('role');
    const username = localStorage.getItem('user');
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

    // Cargar dashboard según el rol.
    if (role === 'admin') {
        import('static/js/admin.js').then(module => module.renderAdminDashboard(content));
    } else if (role === 'fletero') {
        import('static/js/fletero.js').then(module => module.renderFleteroDashboard(content));
    }
    else {
        import('static/js/cliente.js').then(module => module.renderClienteDashboard(content));
    }
});
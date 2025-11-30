document.addEventListener('DOMContentLoaded', async () => {
    const role = localStorage.getItem('role');
    const username = localStorage.getItem('username');
    const token = localStorage.getItem('token');
    const content = document.getElementById('content');

    if (!token) {
        window.location.href = '/login';
        return;
    }

    document.getElementById('username').textContent = username;

    document.getElementById('logoutBtn').addEventListener('click', () => {
        localStorage.clear();
        window.location.href = '/login';
    });

    try {
        const res = await fetch('/api/dashboard', {
            headers: { 
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json'
            }
        });

        const data = await res.json();   

        if (!res.ok) {
            alert(data.message || 'Token invalido');
            localStorage.clear();
            window.location.href = '/login'
            return;
        }

        console.log('Datos validos:', data);

        // Cargar dashboard según el rol.
        if (data.user.role === 'admin') {
            import('/static/js/admin.js').then(module => module.renderAdminDashboard(content));
        } 
        else if (data.user.role === 'fletero') {
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
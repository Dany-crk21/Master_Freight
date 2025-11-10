document.addEventListener('DOMContentLoaded', () => {
    const registerForm = document.getElementById('registerForm');

    registerForm.addEventListener('submit', async (e) => {
        e.preventDefault();
    
              const role = e.target.role.value.trim().toLowerCase();
        const data = {
            username: e.target.username.value.trim(),
            email: e.target.email.value.trim(),
            password: e.target.password.value.trim()
        };

        const endpoint = `/register/${role}`

        try {
            const res = await fetch(endpoint, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });
            const result = await res.json();

            if (res.ok) {
                 alert(`✅ ${result.message}`);
                window.location.href = '/login';
            } else {
                alert(`❌ ${result.message || 'Error al registrar usuario'}`);
            }
        } catch (err) {
            console.error('Error:', err);
            alert('⚠️ Error de conexión con el servidor');
        }
    });
});
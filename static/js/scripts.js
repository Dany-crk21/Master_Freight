document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('loginForm');

    loginForm.addEventListener('submit', async(e) => {
        e.preventDefault();

        const data = {
            email: e.target.email.value,
            password: e.target.password.value
        };

        try {
            const res = await fetch('/login', { 
            method: 'POST',
            headers: {'Content-Type':'application/json'},
            body: JSON.stringify(data)
        });

            const result = await res.json();

            if (res.ok) {
                localStorage.setItem('token', result.token);
                localStorage.setItem('role', result.role);
                localStorage.setItem('user', result.username);
                window.location.href = '/dashboard';
            } else {
                    alert(result.message);
            }
        } catch (err) {
            console.error('Error en login:', err);
            alert('Error al conectar con el servidor');
        }
    });

    const registerForm = document.getElementById('registerForm');
    
    registerForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        const role = e.target.role.value;
        const data = {
            username: e.target.username.value,
            email: e.target.email.value,
            password: e.target.password.value
        };

        // Definir endpoint según el rol.
        const endpoint = `/register/${role} `
               
        try {
            const res = await fetch(endpoint, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });

            const result = await res.json();

            if (res.ok) {
                alert(result.message);
                window.location.href = '/login';
            } else {
                alert(result.message);
            }
        } catch (err) {
            console.error('Error en registro:', err);
            alert('Error al conectar con el servidor');
        }
    });
});
    

    
        
// login
document.getElementById('loginForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const data = {
        email: document.getElementById("email").value,
        password: document.getElementById("password").value
    };
   const res = await fetch('/api/login', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data) });

        const result = await res.json();

        if (res.ok) {
            // Guardar token y rol en Local Storage
            localStorage.setItem('token', result.token);
            localStorage.setItem('role', result.role);
            localStorage.setItem('username', result.username);

            // Redirigir segun el rol
            if (result.role === 'cliente') {
                window.location.href = "/dashboard";
            } else if (result.role === 'fletero') {
                window.location.href = "/fletero/dashboard";
            } else if (result.role === 'admin') {
                window.location.href = "/dashboard";
            }
        } else {
            alert(result.message || "Credenciales incorrectas");
        }
});
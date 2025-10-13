document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('loginForm');
    const registerForm = document.getElementById('registerForm');

    if (loginForm) {
        /* document.getElementById("loginForm").addEventListener("submit" */ 
        loginForm.addEventListener('submit', async (e) => { 
            e.preventDefault();
            const form = e.target;
            const data = {
                email: form.email.value,
                password: form.password.value
            };
            const res = await fetch("/login", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(data)
            }); 
    const result = await res.json();
    if (res.ok) {
        localStorage.setItem("token", result.token);
        localStorage.setItem("role", result.role);
        localStorage.setItem("user", result.username);
        // redirect based on role
        if (result.role === 'admin') {
            window.location.href = '/admin_dashboard';
        } else {
            window.location.href = "/cliente_dashboard"; // Aca hay que ver como según el role, lo mandamos a /cliente_dashbord o /admin_dashboard
        }   
    } else {
        alert(result.message);
    }
})
}
    if (registerForm) { 
        /* document.getElementById("registerForm")*/
        registerForm.addEventListener("submit", async (e) => {
        e.preventDefault();
        const form = e.target;
        const data = {
            username: form.username.value,
            email: form.email.value,
            password: form.password.value,
            role: form.role.value
        };
        const res = await fetch("/register", {
            method: "POST",
            headers: { "Content-Type": "application/json"},
            body: JSON.stringify(data)
        });
        const result = await res.json();
        if (res.ok) {
            alert("Registro exitoso. Ahora puedes iniciar sesión.");
            window.location.href ='/login';
        } else {
            alert(result.message);
        }
    });
}
});
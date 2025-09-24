document.getElementById("loginForm").addEventListener("submit", async (e) => {
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
        window.location.href = "/cliente_dashboard"; // Aca hay que ver como según el role, lo mandamos a /cliente_dashbord o /admin_dashboard
    } else {
        alert(result.message);
    }
});

document.getElementById("registerForm").addEventListener("submit", async (e) => {
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
        window.Location.href ="/login";
    } else {
        alert(result.message);
    }
});
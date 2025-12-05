import { renderClienteDashboard } from "./cliente_component.js";

document.addEventListener('DOMContentLoaded', async () => {
    const token = localStorage.getItem('token');

    if (!token) {
        console.warn("No hay token - redirigiendo al login");
        return window.location.href = "/login";
    }
     // obtener datos del usuario
    const res = await fetch("/cliente/me", {
        headers: { "Authorization": `Bearer ${token}`}
     });
     const user = await res.json();
     //  Mostrar el nombre
     document.getElementById("username").innerText = user.username;
     document.getElementById("role").innerText = user.role;
     document.getElementById("avatar").src=user.imagen_perfil;

     //render del dashboard
     const container = document.getElementById('clienteContainer');
     renderClienteDashboard(container);

    // Logout
    document.getElementById("logoutBtn").addEventListener("click", () => {
        localStorage.clear();
        window.location.href = "/login";
    });
});
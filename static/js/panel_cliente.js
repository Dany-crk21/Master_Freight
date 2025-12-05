import { renderClienteDashboard } from "./cliente_component.js";

document.addEventListener('DOMContentLoaded', () => {
    const token = localStorage.getItem('token');

    if (!token) {
        console.warn("No hay token - redirigiendo al login");
        return window.location.href = "/login";
    }

    const container = document.getElementById('clienteContainer');
    renderClienteDashboard(container);

    // Logout
    document.getElementById("logoutBtn").addEventListener("click", () => {
        localStorage.clear();
        window.location.href = "/login";
    });
});
document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('loginForm');

    loginForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        const data = {
            email: e.target.email.value,
            password: e.target.password.value
        };

        try {
            const res = await fetch('/login', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });

            const result = await res.json();

        if (res.ok) {
            localStorage.setItem("token", result.token);
    
            if (result.role === "cliente") {
                window.location.href = "/cliente/panel";
            } else if (result.role === "fletero") {
                windows.location.href = "/templates/panel_Fletero.html";
            }
        }
    } catch (err) {
            console.error('Error:', err);
        }
    });
});
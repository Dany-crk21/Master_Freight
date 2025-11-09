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
                localStorage.setItem('token', result.token);
                localStorage.setItem('role', result.role);
                localStorage.setItem('username', result.username);
                window.location.href = '/dashboard';
            } else {
                alert(result.message);
            }
        } catch (err) {
            console.error('Error:', err);
        }
    });
});
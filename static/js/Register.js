document.addEventListener('DOMContentLoaded', () => {
    const registerForm = document.getElementById('registerForm');

    registerForm.addEventListener('submit', async (e) => {
        e.preventDefault();
    
        const role = e.target.role.value;
        const data = {
            username: e.target.username.value,
            email: e.target.email.value,
            password: e.target.password.value
        };

        const endpoint = `/register/${role}`

        try {
            const res = await fetch(endpoint, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json '},
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
            console.error('Error:', err);
        }
    });
});

// register.js
document.getElementById('registerForm').addEventListener('submit', async(e) =>{
    e.preventDefault();
    
    const role = document.getElementById('role').value;
    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    const endpoint = role === 'cliente' ? '/register/cliente' : '/register/fletero';

    const response = await fetch(endpoint, {
        method: 'Post',
        headers:{'Content-Type': 'application/json'},
        body: JSON.stringify({username, email, password})
    })

    const result = await response.json();
    const messageDiv = document.getElementById('message');
    if(response.status === 201){
        messageDiv.innerHTML = '<span class="text-success">${result.message}</span>';
    } else { 
        messageDiv.innerHTML = '<span class="text-danger">${result.message}</span>';
    }
});
document.addEventListener('DOMContentLoaded', async () => {
  const token = localStorage.getItem('token');

  // --- Si no hay token
  if (!token) {
    console.log("Usuario no autenticado, Mostrando Home pública");
    mostrarHomePublica();
    return;
  }
  
  // -- Si hay token, cargar Dasboard
  try {
    const res = await fetch('/api/dashboard', {
      headers: { 'Authorization': `Bearer ${token}` }
    });
      
    const data = await res.json();
    if (!res.ok) {
      console.warn("Token inválido. Mostrando Home pública");
      localStorage.clear();
      mostrarHomePublica();
      return;
    }
    
    mostrarHomeConUsuario(data);
    // ---Usuario autenticado ---

  } catch (error) {
    console.error('Error al verificar el token:', error);
    mostrarHomePublica();
  }
});

// ====================================
// funciones del Home
// ========================

// Home cuando no esta logueado
function mostrarHomePublica() {
  const usernameE1 = document.getElementById("username");
  const roleE1 = document.getElementById("role");
  const imagen = document.getElementById("profilepic");
  const userPanel = document.getElementById("userPanel");
  const loginBtn = document.getElementById("loginBtn");
  const registerBtn = document.getElementById("registerBtn");
  
  if (usernameE1) usernameE1.innerText = "Invitado";
  if (roleE1) roleE1.innertext = "sin cuenta";
  if (imagen) imagen.src = "/static/uploads/default.png";
  if (loginBtn) loginBtn.style.display = "inline-block";
  if (registerBtn) registerBtn.style.display = "inline-block";
  if (userPanel) userPanel.style.display = "none";
}

// Home cuando está logueado
function mostrarHomeConUsuario(data) {
  const usernameE1 =  document.getElementById("username");
  const roleE1 = document.getElementById("role");
  const imagen = document.getElementById("profilepic");
  const userPanel = document.getElementById("userpanel");
  const loginBtn = document.getElementById("loginBtn");
  const registerBtn = document.getElementById("registerBtn");

  if (usernameE1) usernameE1.innerText = data.user.username;
  if (roleE1) roleE1.innerText = data.user.role;
  if (imagen) imagen.src = (data.user.imagen_perfil) ? data.user.imagen_perfil : "/static/uploads/default.png";
  if (userPanel) userPanel.style.display = "block";
  if (loginBtn) loginBtn.style.display = "none";
  if (registerBtn) registerBtn.style.display = "none";
  document.getElementById("role").innerText = data.role.user.role;
}

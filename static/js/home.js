document.addEventListener('DOMContentLoaded', async () => {
  const token = localStorage.getItem('token');

  if (!token) {
    alert('⚠️ No tienes sesión iniciada. Redirigiendo al login...');
    window.location.href = '/login';
    return;
  }

  try {
    const res = await fetch('/home', {
      headers: { 'Authorization': `Bearer ${token}` }
    });

    if (!res.ok) {
      alert('⛔ Sesión expirada o inválida. Inicia sesión nuevamente.');
      localStorage.clear();
      window.location.href = '/login';
    }
  } catch (error) {
    console.error('Error al verificar el token:', error);
    window.location.href = '/login';
  }
});
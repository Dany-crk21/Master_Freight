// Confirmación antes de cancelar un pedido
document.addEventListener('DOMContentLoaded', function() {
	const cancelarBtns = document.querySelectorAll('a.btn-danger');
	cancelarBtns.forEach(function(btn) {
		btn.addEventListener('click', function(event) {
			if (btn.textContent.includes('Cancelar')) {
				const confirmar = confirm('¿Estás seguro de que deseas cancelar este pedido?');
				if (!confirmar) {
					event.preventDefault();
				}
			}
		});
	});
});
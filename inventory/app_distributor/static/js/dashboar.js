function updateCounts() {
    fetch('{% url "dashboard_counts" %}')
        .then(response => response.json())
        .then(data => {
            // Actualiza los contadores en la interfaz
            document.querySelector('.block1 .count').textContent = data.user_count > 0 ? data.user_count : 'No existen datos registrados';
            document.querySelector('.block2 .count').textContent = data.categoria_count > 0 ? data.categoria_count : 'No existen datos registrados';
            document.querySelector('.block3 .count').textContent = data.marca_count > 0 ? data.marca_count : 'No existen datos registrados';
            document.querySelector('.block4 .count').textContent = data.presentacion_count > 0 ? data.presentacion_count : 'No existen datos registrados';
            document.querySelector('.block5 .count').textContent = data.carta_color_count > 0 ? data.carta_color_count : 'No existen datos registrados';
            document.querySelector('.block6 .count').textContent = data.producto_count > 0 ? data.producto_count : 'No existen datos registrados';
        })
        .catch(error => console.error('Error fetching counts:', error));
}

// Llama a la función al cargar la página
document.addEventListener('DOMContentLoaded', updateCounts);
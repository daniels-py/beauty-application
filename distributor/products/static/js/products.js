alert("ejemplo para saber si funciona el js");

$(document).ready(function() {
    // Hacer la petición AJAX al API
    $.ajax({
        url: 'categorias-lista',  // Endpoint de tu API
        method: 'GET',
        success: function(data) {
            // Iterar sobre los datos y construir las filas de la tabla
            let tbody = $('#productos-tbody');
            tbody.empty(); // Limpiar el tbody

            // Aquí estamos iterando sobre 'data', que suponemos es una lista de categorías
            data.forEach(categoria => {
                tbody.append(`
                    <tr>
                        <td>${categoria.id}</td>  <!-- Mostramos el ID de la categoría -->
                        <td>${categoria.nombre}</td>  <!-- Mostramos el nombre de la categoría -->
                        <td>${categoria.descripcion}</td>  <!-- Mostramos la descripción de la categoría -->
                    </tr>
                `);
            });
        },
        error: function(error) {
            console.error('Error al cargar las categorías:', error);
        }
    });
});

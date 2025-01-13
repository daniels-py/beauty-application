
// Usamos AJAX para obtener productos
$(document).ready(function() {
        $.ajax({
            url: 'http://127.0.0.1:8000/api/products/api/admin/api/productos/', // URL de la API
            type: 'GET', // Método GET
            success: function(productos) {
                const tbody = $('#productos-table tbody');
                tbody.empty(); // Limpiamos la tabla

                productos.forEach(function(producto) {
                    tbody.append(`
                        <tr>
                            <td>${producto.id}</td>
                            <td>${producto.nombre}</td>
                            <td>${producto.marca.nombre}</td>
                            <td>${producto.categoria.nombre}</td>
                            <td>${producto.precio}</td>
                            <td>${producto.codigo_barras}</td>
                        </tr>
                    `);
                });
            },
            error: function() {
                alert('Error al cargar los productos');
            }
        });
});
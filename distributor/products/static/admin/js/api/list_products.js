// Usamos AJAX para obtener productos
$(document).ready(function () {
    $.ajax({
        url: 'http://127.0.0.1:8000/api/products/api/admin/api/productos/', // URL de la API
        type: 'GET', // Método GET
        success: function (productos) {
            const tbody = $('#productos-table tbody');
            tbody.empty(); // Limpiamos la tabla

            // Iteramos sobre los productos y creamos una fila para cada uno
            productos.forEach(function (producto) {
                tbody.append(`
                    <tr>
                        <td>${producto.id}</td>
                        <td>${producto.nombre}</td>
                        <td>${producto.marca.nombre}</td>
                        <td>${producto.categoria.nombre}</td>
                        <td>${producto.presentacion.nombre}</td>
                        <td>${producto.carta_color ? producto.carta_color.nombre_color : 'No aplica'}</td>
                        <td>${producto.precio}</td>
                        <td>${producto.codigo_barras}</td>
                        <td>
                            <button class="btn-update" data-id="${producto.id}">Actualizar</button>
                            <button class="btn-delete" data-id="${producto.id}">Eliminar</button>
                        </td>
                    </tr>
                `);
            });

            // Evento para actualizar producto
            $('.btn-update').click(function () {
                const id = $(this).data('id'); // Obtiene el ID del producto
                actualizarProducto(id);
            });

            // Evento para eliminar producto
            $('.btn-delete').click(function () {
                const id = $(this).data('id'); // Obtiene el ID del producto
                eliminarProducto(id);
            });
        },
        error: function () {
            alert('Error al cargar los productos');
        }
    });
});

// Función para eliminar producto
function eliminarProducto(id) {
    if (confirm("¿Estás seguro de que deseas eliminar este producto?")) {
        $.ajax({
            url: `http://127.0.0.1:8000/api/products/api/admin/api/productos/${id}/`, // URL para eliminar
            type: 'DELETE',
            success: function () {
                alert('Producto eliminado con éxito');
                location.reload(); // Recarga la página para actualizar la lista
            },
            error: function () {
                alert('Error al eliminar el producto');
            }
        });
    }
}

// Función para actualizar producto (debes agregar tu lógica aquí)
function actualizarProducto(id) {
    alert("Función para actualizar producto con ID: " + id);
    // Aquí puedes agregar el código para redirigir a una página de actualización o mostrar un formulario.
}

$(document).ready(function () {
    $.ajax({
        url: 'http://127.0.0.1:8000/api/inventory/inventarios/', // URL de la API
        type: 'GET', // Método GET
        success: function (inventarios) {
            const tbody = $('#inventario-table tbody');
            tbody.empty(); // Limpiamos la tabla

            // Iteramos sobre el inventario y creamos una fila para cada uno
            inventarios.forEach(function (inventario) {
                tbody.append(`
                    <tr data-id="${inventario.id}">
                        <td>${inventario.id}</td>
                        <td>${inventario.producto_nombre}</td>
                        <td>${inventario.unidades}</td>
                        <td>${inventario.fecha_ingreso}</td>
                        <td>${inventario.precio_producto}</td>
                        <td>
                            <button class="btn-update" data-id="${inventario.id}">Actualizar</button>
                            <button class="btn-delete" data-id="${inventario.id}">Eliminar</button>
                        </td>
                    </tr>
                `);
            });

            // Evento para actualizar inventario
            $('.btn-update').click(function () {
                const id = $(this).data('id'); // Obtiene el ID del inventario
                actualizarInventario(id);
            });

            // Evento para eliminar inventario
            $('.btn-delete').click(function () {
                const id = $(this).data('id'); // Obtiene el ID del inventario
                eliminarInventario(id);
            });
        },
        error: function () {
            alert('Error al cargar el inventario');
        }
    });
});

// Función para eliminar inventario
function eliminarInventario(id) {
    if (confirm("¿Estás seguro de que deseas eliminar este inventario?")) {
        $.ajax({
            url: `http://127.0.0.1:8000/api/inventory/inventarios/${id}/`, // URL para eliminar
            type: 'DELETE',
            success: function () {
                alert('Inventario eliminado con éxito');
                $(`tr[data-id="${id}"]`).remove(); // Elimina la fila de la tabla
            },
            error: function () {
                alert('Error al eliminar el inventario');
            }
        });
    }
}

// Función para actualizar inventario (debes agregar tu lógica aquí)
function actualizarInventario(id) {
    alert("Función para actualizar inventario con ID: " + id);
    // Aquí puedes agregar el código para redirigir a una página de actualización o mostrar un formulario.
}

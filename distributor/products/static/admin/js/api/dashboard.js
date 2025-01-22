$(document).ready(function () {
    function actualizarUsuarios() {
        $.ajax({
            url: 'http://127.0.0.1:8000/api/users/usuarios/total/', // URL de la API para obtener el total de usuarios
            type: 'GET', // Método GET
            success: function (data) {
                $('#total-usuarios').text(data.total_users + ' activos');
            },
            error: function () {
                $('#total-usuarios').text('Error al cargar');
            }
        });
    }

    function actualizarInventario() {
        $.ajax({
            url: 'http://127.0.0.1:8000/api/inventory/inventarios/stock/', // URL de la API para obtener el total de inventario
            type: 'GET', // Método GET
            success: function (data) {
                $('#total-inventario').text(data.total_inventario + ' items');
            },
            error: function () {
                $('#total-inventario').text('Error al cargar');
            }
        });
    }

    // Llamar a las funciones para cargar los datos inicialmente
    actualizarUsuarios();
    actualizarInventario();

    // Escuchar eventos personalizados para actualizar los contadores
    $(document).on('actualizarContadores', function () {
        actualizarUsuarios();
        actualizarInventario();
    });
});

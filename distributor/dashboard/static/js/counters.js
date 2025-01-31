$(document).ready(function () {
    function actualizarUsuarios() {
        $.ajax({
            url: 'http://127.0.0.1:8000/api/users/usuarios/total/', // URL de la API para obtener el total de usuarios
            type: 'GET', // Método GET
            success: function (data) {
                if (data.total_users) {
                    $('#total-usuarios').text(data.total_users + ' activos');
                } else {
                    $('#total-usuarios').text('Por el momento no se registran datos');
                }
            },
            error: function () {
                $('#total-usuarios').text('Error al cargar los datos de usuarios');
            }
        });
    }

    function actualizarInventario() {
        $.ajax({
            url: 'http://127.0.0.1:8000/api/inventory/inventarios/stock/', // URL de la API para obtener el total de inventario
            type: 'GET', // Método GET
            success: function (data) {
                if (data.total_inventario) {
                    $('#total-inventario').text(data.total_inventario + ' items');
                } else {
                    $('#total-inventario').text('Por el momento no se registran datos');
                }
            },
            error: function () {
                $('#total-inventario').text('Error al cargar los datos de inventario');
            }
        });
    }

    function actualizarProductos() {
        $.ajax({
            url: 'http://127.0.0.1:8000/api/products/productos/total/', // URL de la API para obtener el total de productos
            type: 'GET', // Método GET
            success: function (data) {
                if (data.total_productos) {
                    $('#total-productos').text(data.total_productos + ' productos');
                } else {
                    $('#total-productos').text('Por el momento no se registran datos');
                }
            },
            error: function () {
                $('#total-productos').text('Error al cargar los datos de productos');
            }
        });
    }

    function actualizarMarcas() {
        $.ajax({
            url: 'http://127.0.0.1:8000/api/products/marcas/total/', // URL de la API para obtener el total de marcas que permiten color
            type: 'GET', // Método GET
            success: function (data) {
                if (data.total_marcas) {
                    $('#total-marcas').text(data.total_marcas + ' marcas');
                } else {
                    $('#total-marca').text('Por el momento no se registran datos');
                }
            },
            error: function () {
                $('#total-marca').text('Error al cargar los datos de marcas');
            }
        });
    }

    // Llamar a las funciones para cargar los datos inicialmente
    actualizarUsuarios();
    actualizarInventario();
    actualizarProductos();
    actualizarMarcas();

    // Escuchar eventos personalizados para actualizar los contadores
    $(document).on('actualizarContadores', function () {
        actualizarUsuarios();
        actualizarInventario();
        actualizarProductos();
        actualizarMarcas();
    });
});





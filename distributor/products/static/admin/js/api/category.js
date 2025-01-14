$(document).ready(function () {
    // Variables para el modal
    const modal = $('#update-modal');
    const closeModal = $('.close-modal');

    // Función para abrir el modal y rellenar los campos
    function abrirModalActualizar(id) {
        $.ajax({
            url: `http://127.0.0.1:8000/api/products/api/admin/api/productos/${id}/`,
            type: 'GET',
            success: function (producto) {
                // Rellenar los campos del modal
                $('#update-id').val(producto.id);
                $('#update-nombre').val(producto.nombre);
                $('#update-precio').val(producto.precio);
                $('#update-marca').val(producto.marca.id);
                $('#update-categoria').val(producto.categoria.id);

                // Mostrar el modal
                modal.css('display', 'flex');
            },
            error: function () {
                alert('Error al obtener los datos del producto');
            }
        });
    }

    // Evento para cerrar el modal
    closeModal.click(function () {
        modal.css('display', 'none');
    });

    // Cerrar el modal al hacer clic fuera del contenido
    $(window).click(function (e) {
        if ($(e.target).is(modal)) {
            modal.css('display', 'none');
        }
    });

    // Evento para manejar el envío del formulario
    $('#update-form').submit(function (e) {
        e.preventDefault();

        const id = $('#update-id').val();
        const datosActualizados = {
            nombre: $('#update-nombre').val(),
            precio: parseFloat($('#update-precio').val()),
            marca: parseInt($('#update-marca').val()),
            categoria: parseInt($('#update-categoria').val())
        };

        $.ajax({
            url: `http://127.0.0.1:8000/api/products/api/admin/api/productos/${id}/`,
            type: 'PUT',
            contentType: 'application/json',
            data: JSON.stringify(datosActualizados),
            success: function () {
                alert('Producto actualizado con éxito');
                modal.css('display', 'none'); // Cerrar el modal
                location.reload(); // Recargar la tabla
            },
            error: function () {
                alert('Error al actualizar el producto');
            }
        });
    });

    // Evento para abrir el modal desde el botón actualizar
    $(document).on('click', '.btn-update', function () {
        const id = $(this).data('id');
        abrirModalActualizar(id);
    });
});

// Usamos AJAX para obtener usuarios
$(document).ready(function () {
    $.ajax({
        url: 'http://127.0.0.1:8000/api/users/usuarios/', // URL de la API
        type: 'GET', // Método GET
        success: function (usuarios) {
            const tbody = $('#usuarios-table tbody');
            tbody.empty(); // Limpiamos la tabla

            // Iteramos sobre los usuarios y creamos una fila para cada uno
            usuarios.forEach(function (usuario) {
                tbody.append(`
                    <tr>
                        <td>${usuario.id}</td>
                        <td>${usuario.username}</td>
                        <td>${usuario.email}</td>
                        <td>${usuario.last_name}</td>
                        <td>
                            <button class="btn-update" data-id="${usuario.id}">Actualizar</button>
                            <button class="btn-delete" data-id="${usuario.id}">Eliminar</button>
                        </td>
                    </tr>
                `);
            });

            // Evento para actualizar usuario
            $('.btn-update').click(function () {
                const id = $(this).data('id'); // Obtiene el ID del usuario
                actualizarUsuario(id);
            });

            // Evento para eliminar usuario
            $('.btn-delete').click(function () {
                const id = $(this).data('id'); // Obtiene el ID del usuario
                eliminarUsuario(id);
            });
        },
        error: function () {
            alert('Error al cargar los usuarios');
        }
    });
});

// Función para eliminar usuario
function eliminarUsuario(id) {
    if (confirm("¿Estás seguro de que deseas eliminar este usuario?")) {
        $.ajax({
            url: `http://127.0.0.1:8000/api/usuarios/${id}/`, // URL para eliminar
            type: 'DELETE',
            success: function () {
                alert('Usuario eliminado con éxito');
                location.reload(); // Recarga la página para actualizar la lista
            },
            error: function () {
                alert('Error al eliminar el usuario');
            }
        });
    }
}

// Función para actualizar usuario (debes agregar tu lógica aquí)
function actualizarUsuario(id) {
    alert("Función para actualizar usuario con ID: " + id);
    // Aquí puedes agregar el código para redirigir a una página de actualización o mostrar un formulario.
}

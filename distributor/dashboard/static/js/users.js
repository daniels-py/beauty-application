document.addEventListener('DOMContentLoaded', function() {
    fetchUsers();
});

function fetchUsers() {
    fetch('http://127.0.0.1:8000/api/users/usuarios/')
        .then(response => response.json())
        .then(data => {
            const tbody = document.querySelector('#usuarios-table tbody');
            tbody.innerHTML = '';

            data.results.forEach(user => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${user.id}</td>
                    <td>${user.username}</td>
                    <td>${user.email}</td>
                    <td>${user.last_name}</td>
                    <td>
                        <button class="btn-update" onclick="updateUser(${user.id})">Update</button>
                        <button class="btn-delete" onclick="deleteUser(${user.id})">Delete</button>
                    </td>
                `;
                tbody.appendChild(row);
            });

            document.getElementById('total-users').innerText = data.count;
            document.getElementById('active-users').innerText = data.results.filter(user => user.is_active).length;
        })
        .catch(error => console.error('Error fetching users:', error));
}

function deleteUser(userId) {
    if (confirm('¿Estás seguro de que deseas eliminar este usuario?')) {
        fetch(`http://127.0.0.1:8000/api/users/usuarios/${userId}/`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
            },
        })
        .then(response => {
            if (response.ok) {
                fetchUsers(); // Refresh the user list
            } else {
                console.error('Error deleting user:', response.statusText);
            }
        })
        .catch(error => console.error('Error deleting user:', error));
    }
}

function updateUser(userId) {
    // Implement the update functionality here
    // This could involve opening a modal with a form to update user details
    console.log('Update user:', userId);
}
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


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


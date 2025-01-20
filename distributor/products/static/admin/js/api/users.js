document.addEventListener('DOMContentLoaded', function () {
    const tableBody = document.querySelector('#usuarios-table tbody');

    // Función para cargar usuarios desde la API
    const loadUsuarios = async () => {
        try {
            const response = await fetch('/users/api/');
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            const data = await response.json();
            tableBody.innerHTML = ''; // Limpia el contenido existente

            // Agrega los datos a la tabla
            data.forEach(usuario => {
                const row = `
                    <tr>
                        <td>${usuario.id}</td>
                        <td>${usuario.username}</td>
                        <td>${usuario.email}</td>
                        <td>${usuario.last_name}</td>
                    </tr>
                `;
                tableBody.innerHTML += row;
            });
        } catch (error) {
            console.error('Error al cargar los usuarios:', error);
        }
    };

    // Llama a la función para cargar los usuarios
    loadUsuarios();
});

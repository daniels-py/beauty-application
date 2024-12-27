// Ejecutar el código cuando el DOM esté completamente cargado
$(document).ready(function() {
    alert("ejemplo para saber si funciona el js"); // Alerta para confirmar que el JS está funcionando

    // Hacer una petición AJAX al API para obtener las categorías
    $.ajax({
        url: 'http://127.0.0.1:8000/api/products/admin/categorias/',  // URL del endpoint del API
        method: 'GET',  // Tipo de solicitud HTTP: GET para obtener datos
        success: function(data) {
            // Si la solicitud es exitosa, construir la tabla con los datos obtenidos
            let tbody = $('#productos-tbody');  // Seleccionamos el tbody de la tabla donde se insertarán los datos
            tbody.empty(); // Limpiar cualquier contenido previo en el tbody para evitar duplicados

            // Iterar sobre los datos recibidos (una lista de categorías)
            data.forEach(categoria => {
                // Crear una fila (<tr>) con las celdas (<td>) para cada propiedad de la categoría
                tbody.append(`
                    <tr>
                        <td>${categoria.id}</td>  <!-- Mostrar el ID de la categoría -->
                        <td>${categoria.nombre}</td>  <!-- Mostrar el nombre de la categoría -->
                        <td>${categoria.descripcion}</td>  <!-- Mostrar la descripción de la categoría -->
                        <td>${categoria.permite_color}</td>  <!-- Mostrar la descripción de la categoría -->
                        <!-- Agregar botones de acción para actualizar y eliminar -->
                        <td>
                            <button class="btn-actualizar" data-id="${categoria.id}">Actualizar</button>
                            <button class="btn-eliminar" data-id="${categoria.id}">Eliminar</button>
                        </td>
                    </tr>
                `);
            });

            // Añadir funcionalidad a los botones "Actualizar" y "Eliminar"
            $('.btn-actualizar').on('click', function() {
                const id = $(this).data('id'); // Obtener el ID de la categoría asociada
                alert(`Actualizar categoría con ID: ${id}`); // Alerta para verificar funcionalidad
                // Aquí puedes agregar la lógica para actualizar
            });

            $('.btn-eliminar').on('click', function() {
                const id = $(this).data('id'); // Obtener el ID de la categoría asociada
                alert(`Eliminar categoría con ID: ${id}`); // Alerta para verificar funcionalidad
                // Aquí puedes agregar la lógica para eliminar
            });
        },
        error: function(error) {
            // Si hay un error en la solicitud, se muestra en la consola
            console.error('Error al cargar las categorías:', error);
        }
    });
});

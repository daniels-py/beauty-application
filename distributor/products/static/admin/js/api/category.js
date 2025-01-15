document.addEventListener('DOMContentLoaded', function () {
    const tableBody = document.querySelector('#productos-table tbody');

    // Función para cargar productos desde la API
    const loadProductos = async () => {
        try {
            const response = await fetch('/productoss/');
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            const data = await response.json();
            tableBody.innerHTML = ''; // Limpia el contenido existente

            // Agrega los datos a la tabla
            data.forEach(producto => {
                const row = `
                    <tr>
                        <td>${producto.id}</td>
                        <td>${producto.nombre}</td>
                        <td>${producto.marca.nombre}</td>
                        <td>${producto.categoria.nombre}</td>
                        <td>${producto.presentacion.nombre}</td>
                        <td>${producto.precio}</td>
                        <td>${producto.presentacion}</td>
                        <td>${producto.codigo_barras}</td>
                        <td>
                            <button class="btn-accion editar" data-id="${producto.id}">Editar</button>
                            <button class="btn-accion eliminar" data-id="${producto.id}">Eliminar</button>
                        </td>
                    </tr>
                `;
                tableBody.innerHTML += row;
            });
        } catch (error) {
            console.error('Error al cargar los productos:', error);
        }
    };

    // Llama a la función para cargar los productos
    loadProductos();
});


// Agrega un evento al botón con ID 'submitButton' para ejecutar la función cuando se haga clic en él.
document.getElementById('submitButton').addEventListener('click', function () {
    // Obtiene el valor del campo 'username' del formulario.
    const username = document.getElementById('username').value;
    // Obtiene el valor del campo 'email' del formulario.
    const email = document.getElementById('email').value;
    // Obtiene el valor del campo 'first_name' del formulario.
    const first_name = document.getElementById('first_name').value;
    // Obtiene el valor del campo 'last_name' del formulario.
    const last_name = document.getElementById('last_name').value;
    // Obtiene el valor del campo 'password' del formulario.
    const password = document.getElementById('password').value;
    // Obtiene el valor del campo 'confirm_password' del formulario.
    const confirm_password = document.getElementById('confirm_password').value;

      // Verifica si algún campo está vacío.
      if (!username || !email || !first_name || !last_name || !password || !confirm_password) {
        document.getElementById('responseMessage').textContent = 'Por favor, complete todos los campos.';
        document.getElementById('responseMessage').style.color = 'red';
        return; // Detiene la ejecución si hay campos vacíos.
    }

    // Crea un objeto con los datos recopilados del formulario.
    const data = {
        username: username,
        email: email,
        first_name: first_name,
        last_name: last_name,
        password: password,
        confirm_password: confirm_password
    };

    // Realiza una solicitud POST a la API de registro.
    fetch('http://127.0.0.1:8000/api/users/register/common/', {
        method: 'POST', // Especifica que se usará el método POST.
        headers: {
            'Content-Type': 'application/json' // Indica que los datos enviados están en formato JSON.
        },
        body: JSON.stringify(data) // Convierte el objeto 'data' en una cadena JSON para enviarlo en la solicitud.
    })
    .then(response => response.json()) // Convierte la respuesta de la API en un objeto JSON.
    .then(data => {
        // Selecciona el elemento donde se mostrará el mensaje de respuesta.
        const responseMessage = document.getElementById('responseMessage');

        // Si la API devuelve un token de acceso, significa que el registro fue exitoso.
        if (data.access_token) {
            responseMessage.textContent = '¡Usuario registrado exitosamente!'; // Muestra un mensaje de éxito.
            responseMessage.style.color = 'green'; // Cambia el color del mensaje a verde.
            document.getElementById('registerForm').reset(); // Resetea el formulario.
        } else {
            // Si no hay token, muestra el mensaje de error devuelto por la API.
            responseMessage.textContent = 'Error: ' + JSON.stringify(data);
            responseMessage.style.color = 'red'; // Cambia el color del mensaje a rojo.
        }
    })
    .catch(error => {
        // Si ocurre un error durante la solicitud, lo muestra en la consola y en el mensaje de respuesta.
        console.error('Error:', error);
        document.getElementById('responseMessage').textContent = 'Hubo un error. Intente nuevamente.';
        document.getElementById('responseMessage').style.color = 'red'; // Cambia el color del mensaje a rojo.
    });
});

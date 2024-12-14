document.getElementById('submitButton').addEventListener('click', function () {
    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;
    const first_name = document.getElementById('first_name').value;
    const last_name = document.getElementById('last_name').value;
    const password = document.getElementById('password').value;
    const confirm_password = document.getElementById('confirm_password').value;

    const data = {
        username: username,
        email: email,
        first_name: first_name,
        last_name: last_name,
        password: password,
        confirm_password: confirm_password
    };

    fetch('http://127.0.0.1:8000/api/users/register/common/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        const responseMessage = document.getElementById('responseMessage');
        if (data.access_token) {
            responseMessage.textContent = '¡Usuario registrado exitosamente!';
            responseMessage.style.color = 'green';
            document.getElementById('registerForm').reset();
        } else {
            responseMessage.textContent = 'Error: ' + JSON.stringify(data);
            responseMessage.style.color = 'red';
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('responseMessage').textContent = 'Hubo un error. Intente nuevamente.';
        document.getElementById('responseMessage').style.color = 'red';
    });
});

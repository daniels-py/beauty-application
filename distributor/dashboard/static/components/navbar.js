// Selecciona el botón de perfil y el menú desplegable por sus IDs
const profileButton = document.getElementById('profileButton');
const dropdownMenu = document.getElementById('dropdownMenu');

// Agrega un evento de clic al botón de perfil
profileButton.addEventListener('click', () => {
  // Alterna la clase 'active' en el menú desplegable
  dropdownMenu.classList.toggle('active');
  // Alterna la clase 'active' en la imagen del encabezado
  profileButton.classList.toggle('active');
});

// Agrega un evento de clic al objeto window
window.addEventListener('click', (e) => {
  // Si el clic no es en el botón de perfil ni en el menú desplegable
  if (!profileButton.contains(e.target) && !dropdownMenu.contains(e.target)) {
    // Remueve la clase 'active' del menú desplegable
    dropdownMenu.classList.remove('active');
    // Remueve la clase 'active' de la imagen del encabezado
    profileButton.classList.remove('active');
  }
});

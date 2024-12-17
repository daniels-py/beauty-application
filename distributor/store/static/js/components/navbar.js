// Seleccionar elementos
const menuToggle = document.querySelector(".menu-toggle");
const navbar = document.querySelector(".navbar");

// Toggle del menú
menuToggle.addEventListener("click", () => {
    menuToggle.classList.toggle("open"); // Cambia el estado del ícono hamburguesa
    navbar.classList.toggle("active");  // Activa/desactiva la animación del menú
});

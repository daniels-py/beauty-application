/*===== SHOW NAVBAR =====*/ 
// Función para mostrar el navbar y ajustar el cuerpo y el header
const showNavbar = (toggleId, navId, bodyId, headerId) => {
    // Obtiene los elementos por sus IDs
    const toggle = document.getElementById(toggleId),
        nav = document.getElementById(navId),
        bodypd = document.getElementById(bodyId),
        headerpd = document.getElementById(headerId)
    
    // Verifica que todos los elementos existen antes de proceder
    if(toggle && nav && bodypd && headerpd){
        // Añade un evento 'click' al botón de toggle
        toggle.addEventListener('click', () => {
            // Muestra/oculta el navbar alternando la clase 'show'
            nav.classList.toggle('show')
            // Cambia el ícono del botón (entre menú y 'x')
            toggle.classList.toggle('bx-x')
            // Ajusta el padding del body cuando el navbar está visible
            bodypd.classList.toggle('body-pd')
            // Ajusta el padding del header cuando el navbar está visible
            headerpd.classList.toggle('body-pd')
        })
    }
}

// Llama a la función con los IDs de los elementos
// 'header-toggle' => botón para mostrar el menú
// 'nav-bar' => contenedor del navbar
// 'body-pd' => cuerpo principal
// 'header' => encabezado
showNavbar('header-toggle', 'nav-bar', 'body-pd', 'header')

/*===== LINK ACTIVE =====*/ 
// Selecciona todos los enlaces dentro del navbar
const linkColor = document.querySelectorAll('.nav__link')

// Función para activar el enlace clickeado
function colorLink() {
    // Verifica que haya enlaces seleccionados
    if(linkColor){
        // Elimina la clase 'active' de todos los enlaces
        linkColor.forEach(l => l.classList.remove('active'))
        // Agrega la clase 'active' al enlace actual
        this.classList.add('active')
    }
}

// Agrega un evento de clic a cada enlace para activar la función
linkColor.forEach(l => l.addEventListener('click', colorLink))


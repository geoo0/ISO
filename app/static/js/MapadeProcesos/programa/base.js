const subMenuBtns = document.querySelectorAll(".submenu-btn");
subMenuBtns.forEach(btn => {
    btn.addEventListener("click", function(event) {
    event.preventDefault();
    const subMenu = this.nextElementSibling;
    subMenu.style.height = subMenu.style.height ? "" : subMenu.scrollHeight + "px";
    });
});

var modal = document.getElementById('modal');
var closeModalButton = document.getElementsByClassName('close')[0];
var openModalButton = document.getElementById('open-modal');

// Función para abrir el modal y cargar el PDF
function openPdfModal(pdfUrl) {
  var pdfContainer = document.getElementById('pdf-container');
  
  // Muestra el modal
  modal.style.display = 'block';
  
  // Crea un elemento iframe para mostrar el PDF
  var iframe = document.createElement('iframe');
  iframe.src = pdfUrl;
  iframe.style.width = '100%';
  iframe.style.height = '100%';
  
  // Limpia el contenedor del PDF y agrega el iframe
  pdfContainer.innerHTML = '';
  pdfContainer.appendChild(iframe);
}

// Manejador de eventos para abrir el modal cuando se hace clic en el enlace
var menuContenidoLinks = document.getElementsByClassName('menu_contenido');
Array.from(menuContenidoLinks).forEach(function(link) {
  link.addEventListener('click', function(event) {
    event.preventDefault();
    var pdfUrl = this.getAttribute('href');
    openPdfModal(pdfUrl);
  });
});

// Manejador de eventos para cerrar el modal cuando se hace clic en el botón "X"
closeModalButton.addEventListener('click', function() {
  modal.style.display = 'none';
});

// Manejador de eventos para cerrar el modal cuando se hace clic fuera del área del modal
window.addEventListener('click', function(event) {
  if (event.target == modal) {
    modal.style.display = 'none';
  }
});

// Bloquear la combinación de teclas Ctrl + P


//Busqueda 
function buscarEnlaces() {
  // Obtener el valor de entrada del usuario y convertirlo a minúsculas
  var textoBusqueda = document.getElementById("busqueda").value.toLowerCase();
  
  // Obtener todos los elementos con la clase "menu_busqueda" y convertir su texto a minúsculas
  var enlaces = document.querySelectorAll(".menu_busqueda");

  // Variable para controlar si se encontraron coincidencias
  var seEncontraronCoincidencias = false;

  // Recorrer todos los elementos con la clase "menu_busqueda" para ocultarlos o mostrarlos
  enlaces.forEach(function(enlace) {
    var textoEnlace = enlace.textContent.toLowerCase(); // Convertir el texto del enlace a minúsculas
    if (textoEnlace.includes(textoBusqueda)) {
      enlace.style.display = "block"; // Mostrar el enlace
      seEncontraronCoincidencias = true;
    } else {
      enlace.style.display = "none"; // Ocultar el enlace
    }
  });

  // Obtener todos los submenús
  var subMenus = document.querySelectorAll(".submenu");

  // Variable para controlar la visibilidad de los submenús
  var mostrarSubMenu = false;

  // Iterar sobre los submenús y sus enlaces para mostrar u ocultar según la coincidencia
  subMenus.forEach(function(subMenu) {
    var enlacesSubMenu = subMenu.querySelectorAll(".menu_busqueda");
    enlacesSubMenu.forEach(function(enlace) {
      var textoEnlace = enlace.textContent.toLowerCase(); // Convertir el texto del enlace a minúsculas
      if (textoEnlace.includes(textoBusqueda)) {
        enlace.style.display = "block"; // Mostrar el enlace
        // Mostrar el submenú si hay coincidencias en ese submenú
        mostrarSubMenu = true;
      }
    });

    // Mostrar u ocultar el submenú según la variable mostrarSubMenu
    if (mostrarSubMenu) {
      subMenu.style.height = subMenu.scrollHeight + "px"; // Mostrar el submenú
    } else {
      subMenu.style.height = ""; // Ocultar el submenú
    }

    // Restablecer la variable mostrarSubMenu para el siguiente submenú
    mostrarSubMenu = false;
  });

  // Mostrar todos los elementos si no se encontraron coincidencias
  if (!seEncontraronCoincidencias) {
    enlaces.forEach(function(enlace) {
      enlace.style.display = "block"; // Mostrar el enlace
    });
  }
}
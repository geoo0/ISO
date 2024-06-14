// Obtener referencia al botón y al modal
var modalButton = document.getElementById("modalButton");
var modal = document.getElementById("modal");

// Obtener referencia al elemento de cierre del modal
var close = document.getElementsByClassName("close")[0];

// Abrir el modal cuando se haga clic en el botón
modalButton.onclick = function() {
  modal.style.display = "block";
};

// Cerrar el modal cuando se haga clic en el elemento de cierre
close.onclick = function() {
  modal.style.display = "none";
};

// Cerrar el modal cuando se haga clic fuera del área del modal
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
};


// Seleccionamos el titulo
const titulo = document.getElementById('miTitulo');

// Seleccionamos el boton
const boton = document.getElementById('miBoton');

// Cambiamos el color del titulo a rojo
titulo.style.color = 'blue' ;

// Agregamos un "escuchador de eventos" al boton
boton.addEventListener('click', function() {
  // Cuando se haga clic cambia el color de fondo del body
  document.body.style.backgroundColor = 'lightblue';
});
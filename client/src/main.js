
// **************************************************************************************
// **************************************************************************************

//----------    Menú Hamburguesa desplegable    ----------//
const iconoMenu = document.querySelector(".icono-menu");
const menu = document.querySelector(".cont-menu");
const menuMobile = document.querySelector(".icono-menu");

iconoMenu.addEventListener("click", function () {
  menu.classList.toggle("active");
  menuMobile.classList.toggle("active");
  document.body.classList.toggle("opacity");
});

// **************************************************************************************
// **************************************************************************************
// let menu = document.getElementById("menu")
// let botonOpen = document.getElementById("open");
// let botonClose = document.getElementById("close");

// botonOpen.addEventListener("click",()=>{
// 	menu.style.display="flex"
// })

// botonClose.addEventListener("click",()=>{
// 	menu.style.display="none";
// });

// **************************************************************************************
// **************************************************************************************


let activeSlide = 0;
let slides = document.querySelectorAll('.slide');

setInterval(() => {
    slides[activeSlide].classList.remove('activate');
    activeSlide = (activeSlide + 1) % slides.length;
    slides[activeSlide].classList.add('activate');
}, 5000);

// **************************************************************************************
// **************************************************************************************

// // Selecciona el elemento del contador
// var clientesSatisfechosCounter = document.getElementById('clientes-satisfechos-counter');

// // Define el valor final del contador
// var valorFinal = 50;

// // Define la duración de la animación en milisegundos
// var duracionAnimacion = 2000; // 2000 milisegundos = 2 segundos

// // Calcula la cantidad de incremento por milisegundo
// var incrementoPorMilisegundo = valorFinal / duracionAnimacion;

// // Inicializa el contador
// var contador = 0;

// // Crea una función para actualizar el contador
// function actualizarContador() {
//   contador += incrementoPorMilisegundo;
  
//   // Redondea el contador para evitar números decimales innecesarios
//   contador = Math.round(contador);
  
//   // Actualiza el contenido del elemento del contador
//   clientesSatisfechosCounter.innerHTML = contador;

//   // Detén la animación cuando se alcanza el valor final
//   if (contador >= valorFinal) {
//     clearInterval(intervalo);
//     clientesSatisfechosCounter.innerHTML = valorFinal;
//   }
// }

// // Actualiza el contador cada milisegundo
// var intervalo = setInterval(actualizarContador, 1);
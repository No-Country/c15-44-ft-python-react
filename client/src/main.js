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
let slides = document.querySelectorAll(".slide");

setInterval(() => {
  slides[activeSlide].classList.remove("activate");
  activeSlide = (activeSlide + 1) % slides.length;
  slides[activeSlide].classList.add("activate");
}, 5000);

// **************************************************************************************
// **************************************************************************************

let activeTextSlide = 0;
let textSlides = document.querySelectorAll(".text-slide");

setInterval(() => {
  textSlides[activeTextSlide].classList.remove("text-activate");
  activeTextSlide = (activeTextSlide + 1) % textSlides.length;
  textSlides[activeTextSlide].classList.add("text-activate");
}, 5000);

// Code for fetching events from the API
const apiUrl = "/events/?country_id=1";

fetch(apiUrl, { method: "GET", port: 8000 })
  .then((response) => response.json())
  .then((data) => {
    // Process the data from the API and update your DOM as needed
    const exploreContent = document.querySelector(".explore-content");

    data.forEach((event) => {
      // Create a new div for each event
      const eventDiv = document.createElement("div");
      eventDiv.classList.add("sites");

      // Determine the image based on event.id
      let imageName = "a3";
      if (event.id === 1) {
        imageName = "d1";
      } else if (event.id === 2) {
        imageName = "d2";
      } else if (event.id === 3) {
        imageName = "d3";
      } else if (event.id === 4) {
        imageName = "d4";
      } else if (event.id === 5) {
        imageName = "d5";
      } else if (event.id === 6) {
        imageName = "d6";
      } else if (event.id === 7) {
        imageName = "d7";
      } else if (event.id === 8) {
        imageName = "d8";
      } // Add more conditions as needed

      // Add image
      const img = document.createElement("img");
      img.src = `./assets/img/${imageName}.jpg`; // Adjust the property name based on your API response
      img.alt = event.name;
      eventDiv.appendChild(img);

      // Add title
      const title = document.createElement("h5");
      title.textContent = event.name;
      eventDiv.appendChild(title);

      // Add description
      const description = document.createElement("p");
      description.textContent = `Date: ${event.date_and_time}\nAddress: ${event.address}\nPrice: ${event.price}`;
      eventDiv.appendChild(description);

      // Append the new event div to the explore content
      exploreContent.appendChild(eventDiv);
    });
  })
  .catch((error) => console.error("Error fetching data:", error));

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

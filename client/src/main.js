
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


// let activeSlide = 0;
// let slides = document.querySelectorAll('.slide');

// setInterval(() => {
//     slides[activeSlide].classList.remove('active');
//     activeSlide = (activeSlide + 1) % slides.length;
//     console.log(activeSlide)
//     slides[activeSlide].classList.add('active');
// }, 5000);

// console.log(slides.length)
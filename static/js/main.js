window.addEventListener("load", () => {
  // aos initialisation
  AOS.init({
    offset: 200,
    delay: 100,
    duration: 400,
    easing: "ease",
    once: false,
    mirror: false,
    anchorPlacement: "top-bottom",
  });

  // the nav toggle
  const hamburger = document.querySelector(".menutoggle");
  const navMenu = document.querySelector(".nav-list");

  hamburger.addEventListener("click", openMenu);

  function openMenu() {
    navMenu.classList.toggle("active");
  }
  
  window.addEventListener("scroll", ()=>{
    const navSticky = document.querySelector("nav")
    navSticky.classList.toggle("sticky", window.scrollY > 100)
  })
});

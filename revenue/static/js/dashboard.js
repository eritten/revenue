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
  window.addEventListener("scroll", ()=>{
    const navSticky = document.querySelector(".dash-nav")
    navSticky.classList.toggle("sticky", window.scrollY > 100)
  }) 
});

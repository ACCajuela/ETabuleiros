document.addEventListener("DOMContentLoaded", () => {
  const familia = document.getElementById("linkFamilia");

  if (familia) {
    familia.style.cursor = "pointer"; // cursor de link
    familia.addEventListener("click", () => {
      window.location.href = "categoriaFamilia.html";
    });
  }
});
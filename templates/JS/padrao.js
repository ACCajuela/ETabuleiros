document.addEventListener("DOMContentLoaded", () => {
  const familia = document.getElementById("linkFamilia");
  familia.addEventListener("click", () => {
    window.location.href = "categoriaFamilia.html";
  });
});
document.addEventListener("DOMContentLoaded", () => {
  const familia = document.getElementById("linkJogosCartas");
  familia.addEventListener("click", () => {
    window.location.href = "categoriaJogosCartas.html";
  });
});
document.addEventListener("DOMContentLoaded", () => {
  const familia = document.getElementById("linkJogosTabuleiro");
  familia.addEventListener("click", () => {
    window.location.href = "categoriaJogosTabuleiros.html";
  });
});
document.addEventListener("DOMContentLoaded", () => {
  const familia = document.getElementById("linkQuebraCabecas");
  familia.addEventListener("click", () => {
    window.location.href = "categoriaQuebraCabeca.html";
  });
});
document.addEventListener("DOMContentLoaded", () => {
  const familia = document.getElementById("linkRPG");
  familia.addEventListener("click", () => {
    window.location.href = "categoriaRPG.html";
  });
});
document.addEventListener("DOMContentLoaded", () => {
  const familia = document.getElementById("link18");
  familia.addEventListener("click", () => {
    window.location.href = "categoriaProibidao.html";
  });
});
document.addEventListener("DOMContentLoaded", () => {
  const logo = document.getElementById("logoSite");

  if (logo) {
    logo.style.cursor = "pointer";
    logo.addEventListener("click", () => {
      window.location.href = "home.html"; 
    });
  }
});
document.addEventListener("DOMContentLoaded", () => {
  const iconeUsuario = document.getElementById("logoUsuario");

  if (iconeUsuario) {
    iconeUsuario.style.cursor = "pointer";
    iconeUsuario.addEventListener("click", () => {
      const usuarioLogado = localStorage.getItem("usuarioLogado") === "true";

      if (usuarioLogado) {
        window.location.href = "perfil.html";
      } else {
        window.location.href = "login.html";
      }
    });
  }
});
document.addEventListener("DOMContentLoaded", () => {
  const btnCadastro = document.getElementById("btnCadastro");

  if (btnCadastro) {
    btnCadastro.addEventListener("click", () => {
      window.location.href = "cadastro.html";
    });
  }
});





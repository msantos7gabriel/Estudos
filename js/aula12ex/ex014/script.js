var hora = new Date().getHours();
var body = document.querySelector("body");
var divHora = document.getElementById("horas");
var imagem = document.querySelector("section>div>img");
var estado = "";

if (hora <= 12 && hora >= 6) {
  estado = "Manhã";
  imagem.src = "images/amanhecer.jpg";
  body.style.backgroundColor = "#f7dc6f";
} else if (hora > 12 && hora <= 18) {
  estado = "Tarde";
  imagem.src = "images/entardecer.jpg";
  body.style.backgroundColor = "#f39c12";
} else {
  estado = "Noite";
  imagem.src = "images/noite.jpg";
  body.style.backgroundColor = "#5b2c6f";
}

divHora.innerHTML = `<p>Atualmente são ${hora} horas da ${estado}</p>`;

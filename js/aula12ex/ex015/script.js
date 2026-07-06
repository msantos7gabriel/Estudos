var submit = document.getElementById("submit");
submit.addEventListener("click", verificar);

function verificar() {
  var ano = new Date().getFullYear();
  var idade = document.getElementById("txtage").value;
  var sexo = document.getElementsByName("sexo");
  var resposta = document.getElementById("anwser_container");
  var img = document.createElement("img");
  var result_Analize = "";

  // Verificador de Sexo
  if (sexo[0].checked) {
    sexo = "m";
  } else {
    sexo = "f";
  }

  // Verificador de Idade
  if (idade.length == 0 || Number(idade) > ano) {
    alert("ERRO Verifique os dados e tente novamente");
    return;
  } else {
    alert("tudo ok");
  }

  idade = ano - Number(idade);

  if (idade < 5) {
    result_Analize = "bebe";
  } else if (idade >= 5 && idade < 14) {
    result_Analize = "criança";
  } else if (idade >= 14 && idade <= 18) {
    result_Analize = "adolescente";
  } else if (idade > 18 && idade < 65) {
    result_Analize = "adulto";
  } else if (idade >= 65) {
    result_Analize = "idoso";
  }

  // Criando o Atributo da imagem
  img.setAttribute("id", "foto");
  img.setAttribute("alt", "Foto Representando sua idade");
  img.setAttribute("src", `images/${result_Analize}-${sexo}.jpg`);

  resposta.innerHTML = `<p>Dectectamos ${
    sexo == "m" ? "um Homem" : "uma Mulher"
  } de ${idade} anos</p>`;

  resposta.appendChild(img);
}

var submit = document.getElementById("submit");
submit.addEventListener("click", contar);

function contar() {
  var inicio = document.getElementById("inicio");
  var fim = document.getElementById("fim");
  var passo = document.getElementById("passo");
  var res = document.getElementById("anwser_container");

  if (
    inicio.value.length == 0 ||
    fim.value.length == 0 ||
    passo.value.length == 0
  ) {
    res.innerHTML = "<p>Impossivel contar!</p>";
  } else if (Number(passo.value) < 0) {
    alert("Não é possivel fazer a contagem com passo negativo 0");
  } else {
    res.innerHTML = "Contando: ";

    if (Number(passo.value) == 0) {
      passo.value = 1;
    }

    if (Number(inicio.value) > Number(fim.value)) {
      for (
        var i = Number(inicio.value);
        i >= Number(fim.value);
        i -= Number(passo.value)
      ) {
        res.innerText += ` ${i} 👉🏾`;
      }
    } else {
      for (
        var i = Number(inicio.value);
        i <= Number(fim.value);
        i += Number(passo.value)
      ) {
        res.innerText += ` ${i} 👉🏾`;
      }
    }
    res.innerText += "🏁";
  }
}

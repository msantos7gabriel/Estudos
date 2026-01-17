var submit = document.getElementById("submit");
submit.addEventListener("click", calcular);

function calcular() {
  var tabuada = document.getElementById("tabuada");
  var n1 = document.getElementById("n1");

  if (n1.value.length == 0) {
    alert("Por favor, Digite um número");
  } else {
    n1 = Number(n1.value);

    tabuada.innerHTML = "";

    for (var i = 1; i <= 10; i++) {
      var option = document.createElement("option");
      option.innerText = `${n1} x ${i} = ${n1 * i}`;
      tabuada.appendChild(option);
    }
    tabuada.setAttribute("size", 10);
  }
}

var lista_num = [];
let add = document
  .getElementById("adicionar")
  .addEventListener("click", adding);

let final = document
  .getElementById("finalizar")
  .addEventListener("click", ending);

function adding() {
  let txtnum = document.getElementById("txtnumber");
  let intnum = Number(txtnum.value);
  let select = document.getElementById("lista_numeros");
  let option = document.createElement("option");

  if (txtnum.value == "") {
    alert("Valor Invalido: Valor não digitado");
  } else if (intnum > 100 || intnum < 1) {
    alert("Valor Invalido: Valor não se encontra no intervalo solicitado");
  } else if (lista_num.indexOf(intnum) != -1) {
    txtnum.value = "";
    alert("Valor Invalido: Valor já se encontra na Lista");
  } else {
    lista_num.push(intnum);
    option.innerText = `Valor ${intnum} adicionado`;
    select.appendChild(option);
    txtnum.value = "";
  }
}

function ending() {
  let resultado = document.getElementById("resultado");
  lista_num.sort();

  // https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce
  let soma = lista_num.reduce((acumulador, valorAtual) => {
    return acumulador + valorAtual;
  }, 0);

  let media = soma / lista_num.length;
  resultado.innerHTML = "";
  resultado.innerHTML += `<p>Ao todo temos ${lista_num.length} números cadastrados</p>`;
  // da pra usar mim e max mas eu preferi usar o sort e com isso economizar operações
  resultado.innerHTML += `<p>O maior valor informado foi ${lista_num[lista_num.length - 1]}</p>`;
  resultado.innerHTML += `<p>O menor valor informado foi ${lista_num[0]}</p>`;
  resultado.innerHTML += `<p>Somando todos os valores, temos ${soma}</p>`;
  resultado.innerHTML += `<p> A média dos valores digitados é ${media.toFixed(2)}</p>`;
}

let valores = [1, 2, 4, 7, 4, 3, 2, 9, 0];
valores.sort();

for (let i = 0; i < valores.length; i++) {
  console.log(valores[i]);
}

for (pos in valores) {
  console.log(valores[pos]);
}

console.log(valores.indexOf(9));

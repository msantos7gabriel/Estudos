var idade = 67;

if (idade < 16) {
  console.log("Não Vota");
} else {
  if (idade >= 18 && idade <= 65) {
    console.log("Voto obrigatório");
  } else {
    console.log("Vota, mas não é obrigatório");
  }
}

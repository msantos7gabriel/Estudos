var hora = 23;

console.log(`Agora são Exatamente ${hora} Horas`);
if (0 < hora && hora < 5) {
  console.log("Boa Madrugrada");
} else if (hora <= 12) {
  console.log("Bom dia");
} else if (hora <= 18) {
  console.log("Boa Tarde");
} else {
  console.log("Boa Noite");
}

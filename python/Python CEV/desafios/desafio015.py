dias_alugado = int(input('Quantos dias alugados? '))
km_rodados = int(input('Quantos Quilômetros Rodados? '))
valor = (dias_alugado*60)+(km_rodados*0.15)
print("O Total a Pagar é de R${:.2f}".format(valor))
valor_casa = float(input("Qual o valor da casa: "))
salario = float(input("Quanto é o seu salario: ")) * 0.3
tempo = int(input("em quantos anos pretende pagar a casa: ")) * 12

prestacao = valor_casa/tempo

if prestacao > salario:
    print('Empréstimo Negado')
else:
    print('Empréstimo Aprovado')


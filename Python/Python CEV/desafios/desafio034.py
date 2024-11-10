salario = float(input('Escreva seu salario: '))

if salario > 1250:
    salario *= 1.1
else:
    salario *= 1.15

print('Seu novo salario: {:.2f}'.format(salario))
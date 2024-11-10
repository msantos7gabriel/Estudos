peso = float(input('Peso (Kg)'))
altura = pow(float(input('Altura em metros (Ex: 1.80)')), 2)
imc = peso / altura

print('IMC: {:.2f}'.format(imc))

if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Peso Ideal')
elif imc >= 25 and imc < 30:
    print('Sobrepeso')
elif imc >= 30 and imc <= 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')

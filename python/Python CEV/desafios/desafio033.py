num1 = int(input('Escreva um numero: '))
num2 = int(input('Escreva um numero: '))
num3 = int(input('Escreva um numero: '))

if num1 > num2 and num1 > num3:
    print("O Numero: {} é o maior".format(num1))
if num2 > num1 and num2 > num3:
    print("O Numero: {} é o maior".format(num2))
if num3 > num1 and num3 > num2:
    print("O Numero: {} é o maior".format(num3))

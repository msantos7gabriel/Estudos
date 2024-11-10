num = int(input('Digite um número para calcular seu fatorial: '))
num1 = num
fatorial = num * (num-1)

if num == 0:
    fatorial = 1
elif num == 1:
    fatorial = 1
else:
    num -= 1
    while num != 1:
        num -= 1
        fatorial *= num

print('Fatorial de: {} é: {}'.format(num1, fatorial))
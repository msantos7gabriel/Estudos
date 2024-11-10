s = 0
for i in range(0, 7):
    n1 = int(input('Escreva um numero: '))
    if n1 % 2 == 0:
        s += n1
print('A soma foi de: {}'.format(s))

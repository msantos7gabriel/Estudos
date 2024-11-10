# for c in range(1, 5):
#     n = int(input('Digite um Valor: '))
# print('Fim')
# n = ' '
# while n == 'S':
#     c = int(input('Digite um Valor: '))
#     n = str(input('Quer continuar? [S/N] ')).upper()
# print('Fim')
n = 1
par = 0
impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1

print("Valor de pares: {}\nValor de impares: {}".format(par, impar))

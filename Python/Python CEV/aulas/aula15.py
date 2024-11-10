cont = 1
while cont <= 10:
    print(cont, '-> ', end='')
    cont += 1
print("acabou")

n = s = 0
while n != 999:
    n = int(input("Digite um numero: "))
    s += n
print('A soma vale {}'.format(s))

n = s = 0
while True:
    n = int(input("Digite um numero: "))
    if n == 999:
        break
    s += n
# print('A soma vale {}'.format(s))
print(f'A soma vale {s}')

nome = 'José'
idade = 33
salario = 987.3
print(f'O {nome:_^20} tem {idade} anos e ganha R${salario:.2f}')

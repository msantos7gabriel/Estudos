from uteis import numeros as n

num = int(input('Digite um valor: '))
fat = n.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O Dobro de {num} é {n.dobro(num)}')
print(f'O Triplo de {num} é {n.triplo(num)}')

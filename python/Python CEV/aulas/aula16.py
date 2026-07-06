lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(lanche[0:5])

for count in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[count]} na posição {count}')
print('Comi pra caralho !\n\n\n')

# O de cima e o de baixo dão no mesmo

for pos, comidas in enumerate(lanche):
    print(f'Eu vou comer {comidas} na posição {pos}')
print('Comi pra caralho !\n\n\n')

for comidas in lanche:
    print(f'Eu vou comer {comidas}')
print('\nComi pra caralho !')

print(sorted(lanche))
print(lanche)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a+b
print(a)
print(b)
print(c)
print(c.count(5))  # conta a quantidade de vezes em que o '5' aparece
print(c.index(2, 1))  # Mostra a posição em que o '2' está a partir da posição 1
del (c)  # apaga qualquer variável

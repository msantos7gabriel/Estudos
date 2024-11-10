from random import randint
from re import X
i = 0
nomes = []
while 3 >= i:
    str = input('Escreva o nome do Aluno: ')
    nomes.append(str)
    i += 1

print('O Aluno escolhido foi: {}'.format(nomes[randint(0, 3)]))

from random import shuffle
from re import X
i = 0
nomes = []
while 3 >= i:
    str = input('Escreva o nome do Aluno: ')
    nomes.append(str)
    i += 1

shuffle(nomes)
i = 0
while 3 >= i:
    print("{}. {}".format(i, nomes[i]))
    i += 1

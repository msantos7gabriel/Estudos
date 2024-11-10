from random import randint
from time import sleep
from operator import itemgetter

jogadores = {}
jogadores_ordenados = {}
print('Valores sorteados:')
for i in range(1, 5):
    jogadores[f'jogador{i}'] = randint(1, 6)
    print(f'    O Jogador{i} tirou {jogadores[f'jogador{i}']}')
    sleep(1)
print('-='*15)
print('   == RANKING DOS JOGADORES ==')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, r in enumerate(ranking):
    print(f'    {i+1}° Lugar: {r[0]} com {r[1]}.')
    sleep(1)

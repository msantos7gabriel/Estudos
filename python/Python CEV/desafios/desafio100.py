from time import sleep
from random import randint


nums = [0]*5


def sorteio(nums):
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(5):
        nums[i] = randint(0, 10)
        print(nums[i], end=' ', flush=True)
        sleep(0.5)
    print('PRONTO!')


def soma(lista):
    soma = 0
    for l in lista:
        if l % 2 == 0:
            soma += l
    print(f'Somando os valores pares de {lista}, temos {soma}')


sorteio(nums)
soma(nums)

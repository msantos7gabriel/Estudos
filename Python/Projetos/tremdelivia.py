import pyautogui as py
import pandas as pd
from time import sleep
from random import randint


def abrir_opera():
    py.press('win')
    py.write('opera')
    sleep(1)
    py.press('enter')
    sleep(5)


def votar():
    sleep(2)
    py.hotkey('ctrl', 'shift', 'n')
    sleep(1.5)
    py.write('https://pollie.app/1pkqv', interval=0.1)
    py.press('enter')
    sleep(5)
    py.click(900, 925)
    sleep(1)
    py.press('tab')
    nome = tabelas()
    py.write(nome, interval=0.1)
    py.press('enter')
    sleep(3.5)
    py.click(800, 900)
    sleep(0.5)
    py.click(1800, 1020)
    sleep(2)
    py.hotkey('ctrl', 'w')


def tabelas():
    mas = pd.read_csv('ibge-mas-10000.csv')
    fem = pd.read_csv('ibge-fem-10000.csv')

    mas = mas.drop(columns=['regiao', 'freq', 'rank', 'sexo'])
    fem = fem.drop(columns=['regiao', 'freq', 'rank', 'sexo'])
    nomes = [mas, fem]
    nome = (nomes[randint(0, 1)].loc[randint(0, 10000), 'nome']).capitalize()
    return nome


# Inicialização
qtd_votos = int(input('Quantos votos deseja realizar? '))
votos_realizados = 0
abrir_opera()
for _ in range(qtd_votos):
    try:
        votar()
        votos_realizados += 1
        print(votos_realizados)
        sleep(1)
    except KeyboardInterrupt:
        break

py.hotkey('alt', 'f4')
print(f'{votos_realizados} votos realizados')

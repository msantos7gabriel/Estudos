import pyautogui as py
import pandas as pd
from time import sleep
from random import randint
import argparse

parser = argparse.ArgumentParser(description='...')
parser.add_argument('--browser', help="user fev browser", default="opera")
parser.add_argument('--resx', help="lat and long of A point", default=1920)
parser.add_argument('--resy', help="lat and long of A point", default=1080)
args = parser.parse_args()

browser = args.browser
resx = int(args.resx)
resy = int(args.resy)


def res_conversorx(cordx):
    return cordx * resx / 1920


def res_conversory(cordy):
    return cordy * resy / 1080


def abrir_browser():
    py.press('win')
    py.write(browser)
    sleep(1)
    py.press('enter')
    sleep(3)


def votar():
    # Abrir nova aba anonima
    sleep(0.5)
    py.hotkey('ctrl', 'shift', 'n')
    sleep(0.4)
    # botar a url para o voto
    py.write('https://pollie.app/xa7tf')
    py.press('enter')
    # carregando a pagina
    sleep(3)
    # clicar no botão de concordar com os cookies
    py.click(res_conversorx(900), res_conversory(925))
    # Escreve o nome
    py.press('tab')
    # Escreve um nome aleatório
    nome = tabelas()
    py.write(nome)
    py.press('enter')
    sleep(2.5)
    # Clica no botão de votar
    py.click(res_conversorx(1800), res_conversory(1020))
    sleep(0.3)
    # Fecha a aba
    py.hotkey('alt', 'f4')


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
abrir_browser()

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

from random import randint
import pyautogui as pg
from time import sleep

qtd_votos = (int(input("Quantos votos deseja fazer?: ")))

pg.hotkey("alt", "tab")
sleep(3)

def votar():
    sleep(4)
    pg.moveTo(1500, 415, duration=4)
    pg.click()
    numero = randint(1, 3)
    if numero == 1:
        opcao1()
    elif numero == 2:
        opcao2()
    elif numero == 3:
        opcao3()
    sleep(2)
    pg.hotkey("ctrl", "left")


def opcao1():
    sleep(4.5)
    eixo_y = 520
    for i in range(10):
        pg.moveTo(390, eixo_y, duration=.1)
        pg.click()
        eixo_y += 20


def opcao2():
    sleep(4.5)
    eixo_y = 520
    for i in range(10):
        pg.moveTo(525, eixo_y, duration=.1)
        pg.click()
        eixo_y += 20


def opcao3():
    sleep(4.5)
    eixo_y = 520
    for i in range(10):
        pg.moveTo(670, eixo_y, duration=.1)
        pg.click()
        eixo_y += 20


n = 0

while qtd_votos >= n:
    votar()
    n += 1
    if n % 5 == 0:
        pg.hotkey("ctrl", "f5")
        sleep(10)

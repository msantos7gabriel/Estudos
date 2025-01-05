import pyautogui as py
from time import sleep
import pyperclip  # Biblioteca para manipular o clipboard


def abrir_browser():
    py.press('win')
    py.write('opera')  # Ou o navegador de sua preferência
    sleep(1)
    py.press('enter')
    sleep(3)


def votar():
    # Abrir nova aba anônima
    sleep(2)
    py.hotkey('ctrl', 'shift', 'n')
    sleep(2)
    # Colar a URL no navegador
    py.hotkey('ctrl', 'v')  # Cola a URL copiada
    py.press('enter')
    # Carregando a página
    sleep(6)
    py.click(740, 520)  # Ajuste as coordenadas conforme necessário
    py.click(710, 625)  # Ajuste as coordenadas conforme necessário
    sleep(2)
    py.hotkey('alt', 'f4')


# Inicialização
url = "https://www.metro1.com.br/?enquetes"
pyperclip.copy(url)  # Copia a URL para a área de transferência
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

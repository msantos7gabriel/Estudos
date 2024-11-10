from keyboard_cipher import Keyboard_cipher as kc
from os import system


def ask_continue():
    try:
        while True:
            continue_choice = str(
                input('Deseja Continuar ? (S/N): ')).strip().upper()
            if continue_choice == 'N':
                return False
            else:
                return True
    except KeyboardInterrupt:
        program_exit()


def user_choice():
    global user_input
    try:
        while True:
            user_input = int(input('Qual sua escolha ? '))

            if user_input != 1 or user_input != 2:
                return encode_or_decode(user_input)
            else:
                print('Escolha uma opção valida!\n')
    except KeyboardInterrupt:
        program_exit()
    except ValueError:
        print('Escolha uma opção valida!\n')
        user_choice()


def encode_or_decode(user_input):
    global last_frase
    if user_input == 1:
        frase = kc(str(input('Escreva a frase que você deseja codificar: ')))
        last_frase = frase.encode()
    else:
        frase = kc(str(input('Escreva a frase que você deseja decodificar: ')))
        last_frase = frase.decode()


def clear():
    system('cls') or None
    print(f'Ultima Frase', end=' ')
    if user_input == 1:
        print(f'Codificada: {last_frase}')
        print('-'*(25 + len(last_frase)))
    else:
        print(f'Decodificada: {last_frase}')
        print('-'*(27 + len(last_frase)))


def program_exit():
    print('\n\nO Usuário escolheu sair!\nVolte sempre :D')
    exit()

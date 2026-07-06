from time import sleep


cores = (
    '\033[m',         # Sem Cor   - 0
    '\033[0;30;40m',  # Branco   - 1
    '\033[0;30;41m',  # Vermelho - 2
    '\033[0;30;42m',  # Verde    - 3
    '\033[0;30;43m',  # Amarelo  - 4
    '\033[0;30;44m',  # Azul     - 5
    '\033[0;30;45m',  # Roxo     - 6
    '\033[0;30;46m',  # Ciano    - 7
    '\033[0;30;47m',  # Cinza    - 8
)


def ajuda(user):
    user = user.lower()
    titulo(f'Acessando o manual do comando \'{user}\'', 5)
    print(cores[8], end='')
    help(user)
    print(cores[0],end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg)+4
    print(cores[cor], end='')
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)
    print(cores[0], end='')
    sleep(1)


user_input = ''
while True:
    titulo('SISTEMA DE AJUDA pyHELP', 3)
    user_input = str(input('Função ou Biblioteca > ')).upper()
    if user_input == 'FIM':
        break
    ajuda(user_input)
titulo('Até Logo!', 2)

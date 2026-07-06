def leiaInt(string):
    while True:
        try:
            n = str(input(string))
            if n.isnumeric():
                return int(n)
            else:
                print('\033[0;31mERROR! Digite um número inteiro válido.\033[m')
        except (ValueError, TypeError):
            print('\033[0;31mERROR! Digite um número inteiro  válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[0;31mO Usuário preferiu não digitar esse número.\033[m')
            return 0


def leiaFloat(string):
    while True:
        try:
            n = str(input(string))
            if not n.isnumeric():
                return float(n)
            else:
                print('\033[0;31mERROR! Digite um número real válido.\033[m')
        except (ValueError, TypeError):
            print('\033[0;31mERROR! Digite um número real válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[0;31mO Usuário preferiu não digitar esse número.\033[m')
            return 0


n1 = leiaInt('Digite um Número: ')
n2 = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {n1} e o real {n2}')

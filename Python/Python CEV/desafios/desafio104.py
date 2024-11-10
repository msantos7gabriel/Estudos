def leiaInt(string):
    while True:
        n = str(input(string))
        if n.isnumeric():
            return int(n)
        else:
            print('\033[0;31mERROR! Digite um número inteiro válido.\033[m')


n = leiaInt('Digite um Número: ')
print(f'Você acabou de digitar o numero {n}')

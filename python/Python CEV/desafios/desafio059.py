print('--Calculadora--')
n1 = int(input('\nPrimeiro Valor: '))
n2 = int(input('\nSegundo Valor: '))
escolha = ''
while escolha != 5:
    escolha = int(input('''         
    [1] Somar
    [2] multiplicar
    [3] maior
    [4] novos Números
    [5] Sair do Programa
    \n'''))

    if escolha == 1:
        s = n1 + n2
        print("\nA soma de {} e {} se resulta em: {}".format(n1, n2, s))
    elif escolha == 2:
        s = n1 * n2
        print("\nA Multiplicação entre {} e {} se resulta em: {}".format(n1, n2, s))
    elif escolha == 3:
        if n1 > n2:
            print('o Numero: {} é maior'.format(n1))
        else:
            print('o Numero: {} é maior'.format(n2))
    elif escolha == 4:
        n1 = int(input('\nDigite um numero: '))
        n2 = int(input('\nDigite outro numero: '))
    elif escolha == 5:
        print('Saindo do Programa...')
    else:
        print('\nEscreva um valor correto')
    print("=-="*10)
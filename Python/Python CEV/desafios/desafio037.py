print("Conversor de Bases")

valor = int(input('Qual numero que seja ser convertido: '))
escolha = int(input(
    'Escolha a Base em que deseja converter: \n1. Binário\n2. Octal\n3. Hexadecimal\n'))

if escolha == 1:
    binario = bin(valor)
    print('O valor {} convertido para Binário: {}'.format(valor, binario[2:]))
elif escolha == 2:
    octal = oct(valor)
    print('O valor {} convertido para Octal: {}'.format(valor, octal[2:]))
elif escolha == 3:
    hexa = hex(valor)
    print('O valor {} convertido para Hexadecimal: {}'.format(valor, hexa[2:]))
else:
    print('Nenhuma das opções foi escolhida')
    quit()


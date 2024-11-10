while True:
    print('='*30)
    print(f'{'BANCO CEV':^30}')
    print('='*30)
    saque = int(input('Que valor você quer sacar? R$'))

    cinquenta = saque // 50
    resto = saque % 50
    print(f'Total de {cinquenta} cédulas de R$50')
    if resto == 0:
        break
    vinte = resto // 20
    resto = resto % 20
    print(f'Total de {vinte} cédulas de R$20')
    if resto == 0:
        break
    dez = resto // 10
    resto = resto % 10
    print(f'Total de {dez} cédulas de R$10')
    if resto == 0:
        break
    um = resto // 1
    print(f'Total de {um} cédulas de R$1')
    break
print('='*30)
print('Volte Sempre ao BANCO CEV! Tenha um bom dia!')

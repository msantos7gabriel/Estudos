def metade(n):
    return moeda(n*0.5)


def dobro(n):
    return moeda(n*2)


def aumentar(n, aumento):
    return moeda(n * (1 + (aumento/100)))


def reduzir(n, redução):
    return moeda(n * (1 - (redução/100)))


def moeda(valor=0, moeda='R$'):
    return (f'{moeda}{valor:.2f}').replace('.', ',')


def resumo(n, aum, red):
    print('-'*30)
    print(f'{'RESUMO DO VALOR':^30}')
    print('-'*30)
    print(f'{'Preço analisado:':^20}{moeda(n)}')
    print(f'{'Dobro do preço:':^20}{dobro(n)}')
    print(f'{'metade do preço:':^20}{metade(n)}')
    print(f'{f'{aum}% de aumento:':^20}{aumentar(n, aum)}')
    print(f'{f'{red}% de redução:':^20}{reduzir(n, red)}')
    print('-'*30)

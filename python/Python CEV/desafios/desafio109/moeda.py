def metade(n, format=False):
    if format == True:
        return moeda(n * 0.5)
    return n * 0.5


def dobro(n, format=False):
    if format == True:
        return moeda(n * 2)
    return n * 2


def aumentar(n, format=False):
    if format == True:
        return moeda(n * 1.1)
    return n * 1.1


def reduzir(n, format=False):
    if format == True:
        return moeda(n * 0.87)
    return n * 0.87


def moeda(valor=0, moeda='R$'):
    return (f'{moeda}{valor:.2f}').replace('.', ',')

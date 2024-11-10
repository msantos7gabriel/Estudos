def metade(n):
    return n * 0.5


def dobro(n):
    return n * 2


def aumentar(n):
    return n * 1.1


def reduzir(n):
    return n * 0.87


def moeda(valor=0, moeda='R$'):

    return (f'{moeda}{valor:.2f}').replace('.', ',')

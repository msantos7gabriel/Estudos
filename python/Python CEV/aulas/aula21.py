def contador(i, f, p):
    """-> Faz uma contagem e mostra na tela.

    Args:
        i (int): Inicio da contagem
        f (int): Fim da contagem
        p (int): Passo da contagem
    """
    c = i
    while c <= f:
        print(f'{c}', end=' ', flush=True)
        c += p
    print('FIM!')


contador(2, 10, 2)
help(contador)


def somar(a=0, b=0, c=0):
    """-> Função que soma 3 valores e imprime o resultado na tela

    Args:
        a (int, optional): Primeiro valor. Defaults to 0.
        b (int, optional): Segundo valor. Defaults to 0.
        c (int, optional): terceiro valor. Defaults to 0.
    """

    print(f'A soma vale: {a+b+c}')


somar(1, 2, 3)
somar(1, 2)
somar(1)
somar()


def teste():
    x = 8
    print(f'Na função teste, \"n\" vale: {n}')
    print(f'Na função teste, \"x\" vale {x}')


# Programa Principal
n = 2
print(f'No Programa principal, \"n\" vale: {n}')
# print(f'No Programa principal, \"x\" vale: {x}')
teste()


def função():
    n1 = 4
    print(f'N1 dentro vale {n1}')


n1 = 2
função()
print(f'N1 fora vale {n1}')


def teste(b):
    # global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'A dentro vale {b}')
    print(f'A dentro vale {c}')


a = 5
teste(a)
print(f'A fora vale {a}')

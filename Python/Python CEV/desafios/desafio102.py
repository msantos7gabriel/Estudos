
def fatorial(n, show=False):
    """-> Gera um fatorial de um número.

    Args:
        n (int): O número a ser calculado.
        show (bool, optional): Mostra ou não a conta.. Defaults to False.

    Returns:
        int: O Valor do Fatorial de um número n.
    """
    fat = n
    for i in range(n, 1, -1):
        fat *= (i-1)

    if show == True:
        for i in range(n, 1, -1):
            print(i, end=' x ')
        print(f'1 = ', end='')
        return fat
    else:
        return fat


print('-'*30)
print(fatorial(5, True))
print(fatorial(5))

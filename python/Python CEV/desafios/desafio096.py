print(f'{'Controle de Terrenos':^30}')
print('-'*30)


def area(l, c):
    print(f'A área de um terreno {f'{l:.1f}x{c:.1f}'} é de {l*c:.1f}m²')


l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)

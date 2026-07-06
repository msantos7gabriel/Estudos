altura = int(input('Altura da Parede: '))
largura = int(input('Largura da Parede: '))
area = altura * largura
print(
    'A Quantidade de Tinta necessárias para pintar a parede é de {:.1f} Litros de tinta'.format(area/2))

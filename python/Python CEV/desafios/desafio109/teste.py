import moeda

p = float(input('Digite o preço: R$'))
print(f'A Metade de {moeda.moeda(p)} é {moeda.metade(p, False)}')
print(f'O Dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, True)}')
print(f'Reduzindo 13%, temos {moeda.reduzir(p, True)}')

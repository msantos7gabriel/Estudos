import moeda

p = float(input('Digite o preço: R$'))
print(f'A Metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O Dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p))}')

import moeda as m

p = float(input('Digite o preço: R$'))
print(f'A Metade de {p} é {m.metade(p)}')
print(f'O Dobro de {p} é {m.dobro(p)}')
print(f'Aumentando 10%, temos {m.aumentar(p)}')
print(f'Reduzindo 13%, temos {m.reduzir(p)}')
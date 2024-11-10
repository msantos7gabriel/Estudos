# Composição

from classes import Cliente

c1 = Cliente('Luís', 32)
c1.insere_endereço('Belo Horizonte', 'MG')
print(c1.nome)
c1.lista_endereços()
del c1
print()

c2 = Cliente('Maria', 55)
c2.insere_endereço('Salvador', 'BA')
c2.insere_endereço('Rio de Janeiro', 'RJ')
print(c2.nome)
c2.lista_endereços()
del c2
print()

c3 = Cliente('João', 19)
c3.insere_endereço('São Paulo', 'SP')
print(c3.nome)
c3.lista_endereços()
del c3
print()

print('#' * 40)

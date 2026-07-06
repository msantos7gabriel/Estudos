from math import hypot
co = int(input("Escreva o Valor do Cateto Oposto: "))
ca = int(input("Escreva o Valor do Cateto Adjacente: "))
h2 = hypot(co, ca)
print("O comprimento da hipotenusa é igual: {:.2f}".format(h2))

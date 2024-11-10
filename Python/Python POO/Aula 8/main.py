# Agregação

from classes import Carrinho_De_Compras, Produto

carrinho = Carrinho_De_Compras()
p1 = Produto('Camiseta', 50)
p2 = Produto('iphone', 10000)
p3 = Produto('Caneca', 15)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p1)
carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)

carrinho.lista_produtos()
print(carrinho.soma_total())

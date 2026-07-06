tamanho, tipo = map(int, input().split())

estoque = []

for j in range(tamanho):
    estoque.append(list(map(int, input().split())))

n_de_pedidos = int(input())

pedidos = []
for i in range(n_de_pedidos):
    pedidos.append(list(map(int, input().split())))

qtd_pedidos_feitos = 0
for pedido in pedidos:
    if estoque[pedido[0]-1][pedido[1]-1] != 0:
        estoque[pedido[0]-1][pedido[1]-1] -= 1
        qtd_pedidos_feitos += 1

print(qtd_pedidos_feitos)

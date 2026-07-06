dim = int(input())
matriz = []
soma_linhas = [0] * dim
soma_colunas = [0] * dim

# Ler a matriz e calcular as somas das linhas e colunas
for i in range(dim):
    linha = list(map(int, input().split()))
    matriz.append(linha)
    soma_linhas[i] = sum(linha)
    for j in range(dim):
        soma_colunas[j] += linha[j]

# Calcular o peso máximo
peso_maximo = 0
for i in range(dim):
    for j in range(dim):
        peso = soma_linhas[i] + soma_colunas[j] - 2 * matriz[i][j]
        if peso > peso_maximo:
            peso_maximo = peso

print(peso_maximo)

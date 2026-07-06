# Solução Chat GPT

salões, tuneis = map(int, input().split())

# Grafo: lista de sets para acesso rápido
grafo = [set() for _ in range(salões + 1)]  # índice de 1 a S

# Montar o grafo
for _ in range(tuneis):
    a, b = map(int, input().split())
    grafo[a].add(b)
    grafo[b].add(a)

# Sugestões de passeio
n_sugestões = int(input())
sugestões = []
for _ in range(n_sugestões):
    dados = list(map(int, input().split()))
    sugestões.append(dados[1:])  # ignora o primeiro número (tamanho do passeio)

contador = 0

# Verificar cada sugestão
for sugestão in sugestões:
    valido = True
    for i in range(len(sugestão) - 1):
        atual = sugestão[i]
        prox = sugestão[i + 1]
        if prox not in grafo[atual]:
            valido = False
            break
    if valido:
        contador += 1

print(contador)

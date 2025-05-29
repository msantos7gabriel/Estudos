num = int(input())
lista = list(map(int, input().split()))
lista_sorted = sorted(lista)
fora_da_ordem = []
contador = 0

for i in range(num):
    if lista[i] != lista_sorted[i]:
        fora_da_ordem.append(lista[i])
        contador += 1

print(contador)
fora_da_ordem.sort()
for f in fora_da_ordem:
    print(f, end=' ')

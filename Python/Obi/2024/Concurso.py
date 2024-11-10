n, k = map(int, input().split())
notas = sorted(list(map(int, input().split())), reverse=True)
nota_corte = notas[k - 1]
print(nota_corte)

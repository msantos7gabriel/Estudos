centavos = int(input())
resultados = [0]*6

resultados[0] = centavos // 100
centavos %= 100
resultados[1] = centavos // 50
centavos %= 50
resultados[2] = centavos // 25
centavos %= 25
resultados[3] = centavos // 10
centavos %= 10
resultados[4] = centavos // 5
centavos %= 5
resultados[5] = centavos // 1

print(sum(resultados))
for r in resultados:
    print(r)

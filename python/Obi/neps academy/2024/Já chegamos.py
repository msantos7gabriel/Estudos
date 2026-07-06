numeros = list(map(int, input().split()))
listas = []
calculo = []
for i in range(len(numeros)):
    for j in range(len(numeros)):
        if len(calculo)==0:
            calculo.append(numeros[j])
        elif i == j:
            calculo.append(0)
        else:
            calculo.append(calculo[i-1]+numeros[j])
    listas.append(calculo[:])
    calculo.clear()
print(listas)
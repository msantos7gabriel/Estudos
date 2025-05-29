n = int(input())
postes = []
contador = 0
valores = set()

for i in range(n):
    postes.append(int(input()))

for i in range(1, len(postes)+1):
    valores.add(contador)
    try:
        if postes[i]+postes[i-1] < 1000:
            contador += 1
        else:
            contador = 0
        
    except:
        if postes[0] + postes[-1] < 1000:
            contador += 1
        else:
            contador = 0
        valores.add(contador)

print(max(valores))

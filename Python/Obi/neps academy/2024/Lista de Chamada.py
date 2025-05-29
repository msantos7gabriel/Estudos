n, sorteado = map(int, input().split())
presença = []

for i in range(n):
    presença.append(str(input()))
presença.sort()
print(presença[sorteado-1])

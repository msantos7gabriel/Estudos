jogos = list()
for i in range(15):
    n1 = list(map(str, input().split()))
    jogos.append(n1)

quartas = []
j = 0
for i in range(0, 8):
    if int(jogos[i][0]) > int(jogos[i][1]):
        quartas.append(chr(ord('a')+j))
    else:
        quartas.append(chr(ord('a')+(j+1)))
    j += 2


semi = []
j = 0
for i in range(8, 12):
    if int(jogos[i][0]) > int(jogos[i][1]):
        semi.append(quartas[j])
    else:
        semi.append(quartas[j+1])
    j += 2


final = []
j = 0
for i in range(12, 14):
    if int(jogos[i][0]) > int(jogos[i][1]):
        final.append(semi[j])
    else:
        final.append(semi[j+1])
    j += 2

if int(jogos[14][0]) > int(jogos[14][1]):
    print(final[0].upper())
else:
    print(final[1].upper())

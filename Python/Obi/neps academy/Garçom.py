copos_quebrados = 0
n_bandejas = int(input())
for i in range(0, n_bandejas):
    latas, copos = map(int, input().split())
    if latas > copos:
        copos_quebrados += copos
print(copos_quebrados)

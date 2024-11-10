alturas = list(map(int, input().split()))
alturas.sort()

if alturas[0] + alturas[1] > alturas[2]:
    print('S')
else:
    print('N')

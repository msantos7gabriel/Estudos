int(input())
fila = list(map(int, input().split()))

int(input())
saíram = list(map(int, input().split()))

for s in saíram:
    fila.pop(fila.index(s))

for f in fila:
    print(f, end=' ')

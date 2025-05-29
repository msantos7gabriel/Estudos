n = int(input())
lista = list(str(input()))
val = []

i = 0
for l in lista:
    try:
        inicio = i
        while l == lista[i]:
            i += 1
        if lista[inicio:i].count(l) != 0:
            val.append(f'{lista[inicio:i].count(l)} {l}')
    except:
        if lista[inicio:i].count(l) != 0:
            val.append(f'{lista[inicio:i].count(l)} {l}')

for v in val:
    print(v, end=' ')

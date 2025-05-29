lances = []
for i in range(int(input())):
    nome = str(input())
    lance = int(input())
    lances.append({lance: nome})

maior = 0
for lance in lances:
    for key, Value in lance.items():
        if key > maior:
            maior = key
            pessoa = Value

print(pessoa)
print(maior)

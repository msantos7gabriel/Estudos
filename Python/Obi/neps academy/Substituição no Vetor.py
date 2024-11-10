vet = []
ocorrências = []

for _ in range(10):
    vet.append(int(input()))

menor = min(vet)

for i in range(len(vet)):
    if vet[i] == menor:
        vet[i] = -1
        ocorrências.append(i)
print(f'Menor: {menor}')
print(f'Ocorrencias: ', end='')
print(*ocorrências)
print(*vet)

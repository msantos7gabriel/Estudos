n = int(input())
sapatos = []
pares = 0
for i in range(n):
    sapatos.append(str(input()))

for s in sapatos[:]:  # Criar uma cópia para poder remover itens
    if s[3] == 'D':
        if (s[:3]+'E') in sapatos:
            sapatos.remove(s)
            sapatos.remove(s[:3]+'E')
            pares += 1

print(pares)

n_total_estudantes, n_pares_juntos, n_pares_separados = map(
    int, input().split())

preferencias = []
for _ in range(n_pares_juntos):
    preferencias.append(list(map(int, input().split())))

restrições = []
for _ in range(n_pares_separados):
    restrições.append(list(map(int, input().split())))

trios = []
for _ in range((n_total_estudantes // 3)):
    trios.append(list(map(int, input().split())))

irregularidades = 0

for trio in trios:
    for dupla in restrições:
        if dupla[0] in trio and dupla[1] in trio:
            irregularidades += 1

for pares in preferencias:
    for trio in trios:
        if pares[0] in trio:
            if pares[1] not in trio:
                irregularidades += 1
                break

print(irregularidades)

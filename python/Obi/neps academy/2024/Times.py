from operator import itemgetter

n_pessoas, qtd_times = map(int, input().split())
pessoas = []
time = {}

for i in range(n_pessoas):
    nome, habilidade = map(str, input().split())
    pessoas.append([nome, int(habilidade)])

pessoas = sorted(pessoas, key=itemgetter(1), reverse=True)

j = 0
for p in pessoas:
    time[p[0]] = j
    j += 1
    if j == qtd_times:
        j = 0

time = sorted(time.items(), key=itemgetter(1, 0))

for i in range(qtd_times):
    print(f'Time {i+1}')
    for t in time:
        if t[1] == i:
            print(t[0])
    print()

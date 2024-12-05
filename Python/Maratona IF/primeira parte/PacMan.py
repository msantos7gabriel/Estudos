def caminho(i, par):
    global comida
    if par == False:
        tabuleiro[i] = reversed(tabuleiro[i])
    for t in tabuleiro[i]:
        if t == 'o':
            comida += 1
        if t == 'A':
            maior_valor.add(comida)
            comida = 0
    maior_valor.add(comida)

n = int(input())
tabuleiro = []
maior_valor = set()
comida = 0

for _ in range(n):
    tabuleiro.append(list(str(input())))

for i in range(len(tabuleiro)):
    if i % 2 == 0:
        par = True
    else:
        par = False
    caminho(i, par)
print(max(maior_valor))

n_linhas = int(input())
linhas = []
verificador = 0


def ver_linhas():
    for i in range(0, n_linhas):
        soma = 0
        for j in range(0, len(linhas[i])):
            soma += linhas[i][j]
        if soma != verificador:
            return -1
        else:
            continue
    return soma


def ver_colunas():
    for i in range(0, n_linhas):
        soma = 0
        for j in range(0, len(linhas[i])):
            soma += linhas[j][i]
        if soma != verificador:
            return -1
        else:
            continue
    return soma


def ver_diagonal():
    soma = 0
    for i in range(0, n_linhas):
        for j in range(0, len(linhas[i])):
            if i == j:
                soma += linhas[i][j]
    if soma != verificador:
        return -1
    else:
        return soma


def ver_diagonal_inversa():
    j = len(linhas[0])-1
    i = soma = 0
    while j != -1:
        soma += linhas[i][j]
        j -= 1
        i += 1
    if soma != verificador:
        return -1
    else:
        return soma


for i in range(0, n_linhas):
    numeros = list(map(int, input().split()))
    linhas.append(numeros[:])
    numeros.clear()

for k in range(0, 1):
    for l in range(0, len(linhas[k])):
        verificador += linhas[k][l]


if ver_colunas() == verificador and ver_linhas() == verificador and ver_diagonal() == verificador and ver_diagonal_inversa() == verificador:
    print(verificador)
else:
    print(-1)

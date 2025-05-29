def sum_linha():
    for i in range(3):
        soma = 0
        for j in range(3):
            soma += matriz[i][j]
        resultados.add(soma)
    return verificador()


def sum_coluna():
    for i in range(3):
        soma = 0
        for j in range(3):
            soma += matriz[j][i]
        resultados.add(soma)
    return verificador()


def sum_diagonal():
    soma = 0
    for i in range(3):
        for j in range(3):
            if i == j:
                soma += matriz[j][i]
    resultados.add(soma)
    return verificador()


def sum_diagonal_inversa():
    soma = 0
    l = 0
    c = 2
    for i in range(3):
        soma += matriz[l][c]
        l += 1
        c -= 1
    resultados.add(soma)
    return verificador()


def verificador():
    if len(resultados) > 1:
        return 'N'


linha = []
matriz = []
resultados = set()
for i in range(3):
    for j in range(3):
        linha.append(int(input()))
    matriz.append(linha[:])
    linha.clear()

r = 'SIM'
for i in range(i):
    if sum_coluna() == 'N':
        r = 'NAO'
        break
    if sum_linha == 'N':
        r = 'NAO'
        break
    if sum_diagonal() == 'N':
        r = 'NAO'
        break
    if sum_diagonal_inversa() == 'N':
        r = 'NAO'
        break

print(r)
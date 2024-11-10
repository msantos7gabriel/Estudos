heli, policial, fugitivo, direcao = map(int, input().split())

if direcao == -1:
    while True:
        if fugitivo == policial:
            resposta = 'N'
            break
        if fugitivo == heli:
            resposta = 'S'
            break
        if fugitivo == 0:
            fugitivo = 15
        else:
            fugitivo += -1
else:
    while True:
        if fugitivo == policial:
            resposta = 'N'
            break
        if fugitivo == heli:
            resposta = 'S'
            break
        if fugitivo == 15:
            fugitivo = 0
        else:
            fugitivo += 1
print(resposta)

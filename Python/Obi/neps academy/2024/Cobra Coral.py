padrão_cores = list(map(int, input().split()))
primeira_parte = [padrão_cores[0], padrão_cores[1]]
segunda_parte = [padrão_cores[2], padrão_cores[3]]

for i in range(2):
    if primeira_parte[i] == segunda_parte[i]:
        resposta = 'V'
        break
    else:
        resposta = 'F'
print(resposta)
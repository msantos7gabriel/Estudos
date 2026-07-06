n = list(str(input()))
pos = 0
moves = 0

for i in range(len(n)):
    soma = abs(pos - int(n[i]))
    soma_c = 10 - soma
    moves += min(soma, soma_c)
    pos = int(n[i])
print(moves)

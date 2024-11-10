qtd_musicas, vezes_usado = map(int, input().split())

playlist = []
dicio = {}
moves = [0]*vezes_usado
move = 0

for i in range(0, qtd_musicas):
    playlist.append(list(map(str, input().split())))
    playlist[i] = ' '.join(playlist[i])

for i, p in enumerate(playlist):
    dicio[p[p.index(' ')+1:]] = p[0:p.index(' ')]

for i in range(vezes_usado):
    move = str(input())
    moves[i] = move

for i in range(len(moves)):
    if moves[i] not in dicio:
        print('Nao existe musica')
    else:
        print(dicio[moves[i]])

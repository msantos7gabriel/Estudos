jogador = {}
gols = []

jogador['nome'] = str(input('Nome do Jogador: ')).capitalize()
n = int(input(f'Quantas partidas {jogador['nome']} jogou? '))

for i in range(n):
    gols.append(int(input(f'Quantos Gols na partida {i+1}? ')))

jogador['gols'] = gols[:]
jogador['total de gols'] = sum(gols)
print('-='*30)

for k, v in jogador.items():
    print(f'{k}: {v}.')

print('-='*30)
print(f'O Jogador {jogador["nome"]} jogou {n} partidas.')

for i, g in enumerate(gols):
    print(f'    => Na Partida{i+1}, fez {g} gols.')
print(f'foi um total de {jogador['total de gols']} gols.')

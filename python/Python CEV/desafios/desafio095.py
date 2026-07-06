jogador = {}
jogadores = []
gols = []
i = n = 0

while True:
    print('-'*30)
    jogador['cod'] = i
    jogador['nome'] = str(input('Nome do Jogador: ')).capitalize()
    n = int(input(f'Quantas partidas {jogador['nome']} jogou? '))

    for i in range(n):
        gols.append(int(input(f'Quantos Gols na partida {i+1}? ')))
    
    jogador['gols'] = gols[:]
    jogador['total de gols'] = sum(gols)
    jogadores.append(jogador.copy())
    
    while True:
        continuar = str(
            input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if continuar in 'SN':
            break
    if continuar == 'N':
        break
    i += 1

print('-='*25)
print(f'{'cod':<4}{'nome':<15}{'gols':<26}{'Total':6<}')
print('-'*50)

for i in range(len(jogadores)):
    print(f'{str(jogadores[i]['cod']):>3} {jogadores[i]['nome']:<15}{str(jogadores[i]['gols']):<25} {jogadores[i]['total de gols']:<6}')

while True:
    print('-'*50)
    n = int(input('Mostrar levantamento de qual jogador? '))
    if n == 999:
        break
    elif n > len(jogadores):
        print(f'ERRO! Não exite jogador com o código {n}! Tente novamente')
    else:
        print(f'-- LEVANTAMENTO DE DADOS DO JOGADOR {jogadores[n-1]['nome']}')
        for i, g in enumerate(jogadores[n-1]['gols']):
            print(f'    No jogo {i+1}, fez {g} gols.')

print('<< Volte Sempre >>')

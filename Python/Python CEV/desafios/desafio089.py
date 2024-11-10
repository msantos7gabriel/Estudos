boletin = []

while True:
    nome = str(input('\nNome: ').strip().capitalize())
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = n1 + n2 / 2
    boletin.append([nome, [n1, n2], media])
    while True:
        continuar = str(
            input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if continuar in 'SN':
            break
    if continuar == 'N':
        break
print('-='*30)
print(f'{'No.':<4}{'NOME':<10}{'MÉDIA':>8}')
print('-'*30)
for i, r in enumerate(boletin):
    print(f'{i:<4}{r[0]:<10}{r[2]:>8.1f}')
print('-'*30)

while True:
    escolha = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    print('-'*30)
    if escolha == 999:
        print('Finalizando...')
        break
    elif escolha >= len(boletin):
        print(f'Não há aluno n°{escolha}')
    else:
        print(f'As notas de {boletin[escolha][0]} são {boletin[escolha][1]}')
print('<<< VOLTE SEMPRE >>>')

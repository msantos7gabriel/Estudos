def ficha(nome, gols):
    if gols.isnumeric() == False:
        gols = 0
    else:
        gols = int(gols)
    if nome.isalpha() == False:
        nome = '<desconhecido>'

    print(f'O Jogador {nome} fez {gols} gol(s) no campeonato.')


nome_jogador = str(input('Nome do Jogador: '))
numero_de_gols = str(input('Número de Gols: '))
ficha(nome_jogador, numero_de_gols)

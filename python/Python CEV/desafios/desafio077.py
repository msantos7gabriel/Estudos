palavras = ('chuva', 'fogo', 'areia', 'estrela', 'lua',
            'nuvem', 'vento', 'neve', 'raio', 'deserto')

for nomes in palavras:
    print(f'\nNa palavra {nomes.upper()} temos: ', end='')
    for i in range(0, len(nomes)):
        if nomes[i] in 'aeiou':
            print(nomes[i], end=' ')

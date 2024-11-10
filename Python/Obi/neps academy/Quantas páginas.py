n = int(input())
livros = []
livros_paginas = []

for _ in range(n):
    livros.append(list(map(int, input().split())))

for i in range(n):
    qtdl_questão = livros[i][0] * livros[i][1]
    qtdl_resposta = livros[i][0] * livros[i][2]
    linhas = qtdl_questão + qtdl_resposta
    paginas = linhas // livros[i][3]
    if linhas % livros[i][3] != 0:
        paginas += 1
    print(f'O livro contera {paginas} paginas.')

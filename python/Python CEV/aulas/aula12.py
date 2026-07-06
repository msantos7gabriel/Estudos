nome = str(input('Qual é seu Nome? ')).capitalize().strip()
if nome == 'Gustavo':
    print('Que nome Lindo você tem!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}'.format(nome))
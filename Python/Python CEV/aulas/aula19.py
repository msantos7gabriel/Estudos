pessoas = {
    'nome': 'Gustavo',
    'Sexo': 'M',
    'Idade': 22
}
print(f'O {pessoas["nome"]} tem {pessoas["Idade"]} anos.')
print(pessoas.items())

for k in pessoas.keys():
    print(f'Chave: {k}')

for v in pessoas.values():
    print(f'Valor: {v}')

del pessoas['Sexo']
pessoas['nome'] = 'Leandro'
pessoas['Peso'] = 98.5
for k, v in pessoas.items():
    print(f'Chave: {k}, Valor: {v}')

brasil = []

estado1 = {
    'uf': 'Rio De Janeiro',
    'sigla': 'RJ'
}
estado2 = {
    'uf': 'São Paulo',
    'sigla': 'SP'
}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[1]['uf'])

estado = {}
brasil = []
for i in range(3):
    estado['uf'] = str(input('\nUnidade Federativa: ').capitalize())
    estado['sigla'] = str(input('Sigla do Estado: ').upper())
    brasil.append(estado.copy())
for e in brasil:
    for k,v in e.items():
        print(f'O Campo {k} tem valor {v}.')
    print('\n')
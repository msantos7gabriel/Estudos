aluno = {}

aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno['nome']}: '))

if aluno['media'] >= 7:
    aluno['situação'] = 'APROVADO'
else:
    aluno['situação'] = 'REPROVADO'

for k, v in aluno.items():
    print(f'{k} é igual a {v}')

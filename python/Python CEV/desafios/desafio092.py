from datetime import date

pessoa = {}
pessoa['nome'] = str(input('Nome: ').capitalize())
pessoa['idade'] = date.today().year - int(input('Ano de Nascimento: '))
pessoa['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

if pessoa['ctps'] == 0:
    pessoa['ctps'] = 'Não Possui'
else:
    pessoa['contratação'] = int(input('Contratação: '))
    pessoa['salario'] = round(float(input('Salario: ')), 2)
    pessoa['aposentadoria'] = (
        ((pessoa['contratação'] - date.today().year)+35)+pessoa['idade'])
print('-='*30)

for k, v in pessoa.items():
    print(f'{k}: {v}')

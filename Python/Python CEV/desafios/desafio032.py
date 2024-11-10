from datetime import date
ano = int(input('Insira o Ano: '))
if ano == 0:
   ano= date.today().year
if ano % 4 == 0 and ano % 100 != 0:
    print('Ano Bissexto')
else:
    print('Ano Não Bissexto')

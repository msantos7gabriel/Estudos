from datetime import date
nascimento = int(input('Ano de Nascimento: '))
ano_atual = date.today().year
idade = ano_atual - nascimento
print('Quem nasceu em {} tem {} em {}'.format(nascimento, idade, ano_atual))
if idade < 18:
    print('Ainda faltam {} para o seu alistamento'.format(18-idade))
    print('Seu alistamento será em {}'.format((idade - 18)+ano_atual))
elif idade > 18:
    print('Você já deveria ter se alistado há {} anos'.format(idade - 18))
    print('Seu alistamento foi em {}'.format(nascimento+18))
else:
    print('Você tem que se alistar IMEDIATAMENTE!')

nota1 = float(input('Escreva a sua primeira nota: '))
nota2 = float(input('Escreva a sua segunda nota: '))
m = (nota1+nota2)/2

if m < 5:
    print('REPROVADO')
elif m >= 5 and m <= 6.9:
    print('RECUPERAÇÃO')
elif m >= 7:
    print('APROVADO')

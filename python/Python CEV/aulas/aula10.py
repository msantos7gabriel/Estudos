nome = str(input('Qual é seu Nome? ')).capitalize()
if nome == 'Gustavo':
    print('Que nome Lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('Sua Media foi {:.1f}'.format(m))
if m < 6:
    print('Reprovado')
else:
    print('Aprovado')

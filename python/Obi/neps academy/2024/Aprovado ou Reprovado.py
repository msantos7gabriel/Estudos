n1, n2 = map(float, input().split())
n1 = round((n1+n2)/2, 1)

if n1 >= 7:
    print('Aprovado')
elif n1 >= 4:
    print('Recuperacao')
else:
    print('Reprovado')

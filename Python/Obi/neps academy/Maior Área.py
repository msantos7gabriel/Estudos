n1, n2 = map(int, input().split())
n3, n4 = map(int, input().split())

a1 = n1 + n2
a2 = n3 + n4

if a1 > a2:
    print('Primeiro')
elif a2 > a1:
    print('Segundo')
else:
    print('Empate')

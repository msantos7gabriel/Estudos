lista = list(map(int, input().split()))
lista_c = sorted(lista)
lista_d = sorted(lista, reverse=True)

if lista == lista_c:
    print('C')
elif lista == lista_d:
    print('D')
else:
    print('N')

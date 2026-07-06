r = int(input())
f = int(input())
c = int(input())

if f > (r * 3) or c < 95:
    print('diminuir')
elif f < (r * 2) and c > 95:
    print('aumentar')
else:
    print('manter')

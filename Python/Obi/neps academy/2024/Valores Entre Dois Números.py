n1 = int(input())
n2 = int(input())


def maior(n1, n2):
    if n1 >= n2:
        return n1
    else:
        return n2


def menor(n1,n2):
    if n1 <= n2:
        return n1
    else:
        return n2


for i in range(menor(n1, n2), maior(n1, n2)+1):
    print(i, end=' ')

par = int(input())
n1 = int(input())
n2 = int(input())

if par == 0:
    if (n1 + n2) % 2 == 0:
        print(par)
    else:
        print(1)
else:
    if (n1 + n2) % 2 == 0:
        print(par)
    else:
        print(0)

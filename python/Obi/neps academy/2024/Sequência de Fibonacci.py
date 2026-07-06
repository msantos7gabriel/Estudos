n = int(input())
n1 = 0
n2 = 1
for i in range(n):
    if i == 0:
        print(i, end=' ')
    elif i == 1:
        print(i, end=' ')
    else:
        n3 = n1 + n2
        print(n3, end=' ')
        n1 = n2
        n2 = n3

n = int(input())

n1 = n2 = n3 = 1

for i in range(0, n-1):
    n3 = n1+n2
    n1 = n2
    n2 = n3
print(n3)

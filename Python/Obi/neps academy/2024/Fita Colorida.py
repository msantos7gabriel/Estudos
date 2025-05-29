n = int(input())
nums = list(map(int, input().split()))
zeros = []


def distancia(x):
    dist = []
    menor = float('inf')
    for a in zeros:
        dist.append(a-x)
    for d in dist:
        if d < menor:
            if d <= -1:
                d *= -1
            menor = d
    return menor


for i, n in enumerate(nums):
    if n == 0:
        zeros.append(nums.index(n, i))
for j, x in enumerate(nums):
    if x == -1:
        x = distancia(j)
        if x >= 9:
            x = 9
        print(x, end=' ')
    else:
        print(0, end=' ')

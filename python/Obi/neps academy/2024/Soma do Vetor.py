def soma_vetor(n, v):
    total = 0
    for i in range(n):
        total += v[i]
    return total


n = int(input())
v = list(map(int, input().split()))
print(soma_vetor(n, v))

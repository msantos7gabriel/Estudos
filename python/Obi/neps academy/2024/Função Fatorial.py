
def fatorial(n):
    if n == 0:
        return 1
    fat = n
    for i in range(n, 1, -1):
        fat *= (i-1)
    return fat


n = int(input())
print(fatorial(n))

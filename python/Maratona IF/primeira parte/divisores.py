n = int(input())
num_divisores = 0

for i in range(1, n+1):
    if n % i == 0:
        num_divisores += 1
print(num_divisores)

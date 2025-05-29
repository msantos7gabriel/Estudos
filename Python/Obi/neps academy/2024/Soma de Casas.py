n = int(input())
casas = []
for i in range(n):
    casas.append(int(input()))
k = int(input())


r = 0
l = len(casas)-1
while True:
    if casas[r]+casas[l] < k:
        r += 1
    elif casas[r]+casas[l] > k:
        l -= 1
    else:
        nums = str(f'{casas[r]} {casas[l]}')
        break
print(nums)

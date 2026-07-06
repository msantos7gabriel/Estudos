n = int(input())
nums = []
for i in range(n):
    nums.append(str(input()))
verificar = ''.join(nums)

for i in range(0, 10):
    print(f'{i} - {verificar.count(str(i))}')

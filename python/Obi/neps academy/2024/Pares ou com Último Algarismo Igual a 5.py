nums = [0]*3
for i in range(3):
    nums[i] = int(input())
i = 0
for n in nums:
    if n % 2 == 0 or (n % 2 != 0 and n % 5 == 0):
        i += 1
print(i)

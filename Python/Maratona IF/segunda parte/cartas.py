nums = list()
for i in range(3):
    nums.append(int(input()))

for n in nums:
    if nums.count(n) == 1:
        print(n)
        break


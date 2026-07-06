n1 = int(input())
n2 = int(input())
n3 = int(input())
nums = [n1, n2, n3]
nums_sorted = nums[:]
nums_sorted.sort()
for n in nums_sorted:
    print(nums.index(n)+1)

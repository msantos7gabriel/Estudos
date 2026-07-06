int(input())
nums = list(map(int, input().split()))
nums.sort()
for n in nums:
    print(n,end=' ')

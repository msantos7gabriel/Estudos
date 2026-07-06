v, t = map(int, input().split())
nums = list(map(int, input().split()))

for n in nums:
    v += n
    if v > 100:
        v = 100
    if v < 0:
        v = 0

print(v)

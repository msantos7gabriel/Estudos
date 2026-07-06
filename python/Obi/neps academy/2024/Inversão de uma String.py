n, a, b = map(int, input().split())
s = list(str(input()))

for i in range(a-1):
    print(s[i], end='')
for r in list(reversed(s[a-1:b])):
    print(r, end='')
for i in range(b, len(s)):
    print(s[i], end='')

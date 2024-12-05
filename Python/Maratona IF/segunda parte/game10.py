n = int(input())
d = int(input())
a = int(input())

count = 0
while True:
    if d == a:
        print(count)
        break
    count += 1
    a += 1
    if a == n:
        a = 1
        count += 1

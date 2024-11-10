t = int(input())
m = int(input())
a = int(input())

dias = 0
while True:
    if t >= a:
        break
    else:
        t += m * t
        dias += 1
print(dias)

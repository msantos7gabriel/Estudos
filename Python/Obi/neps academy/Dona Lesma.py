a = int(input())
s = int(input())
d = int(input())
pos = dias = 0

while True:
    pos += s 
    dias += 1
    if pos >= a:
        break
    pos -= d
print(dias)

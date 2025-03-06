s = int(input())
a = int(input())
b = int(input())

count = 0 

for i in range(a, b+1):
    soma = 0
    for j in range(len(str(i))):
        i = str(i)
        soma += int(i[j])
    if s == soma:
        count +=1

print(count)
n = int(input())
sum=0
for i in range(0,n+1):
    visitas = int(input())
    sum+=visitas
    if sum >=1000000:
        break
print(i+1)
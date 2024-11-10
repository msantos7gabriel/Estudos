vet = list(map(int, input().split()))
x = int(input())

if vet.count(x) == 0:
    print('Mia x')
else:
    print(vet.count(x))
    for i in range(len(vet)):
        if vet[i] == x:
            print(i, end=' ')

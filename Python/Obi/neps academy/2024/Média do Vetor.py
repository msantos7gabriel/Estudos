from statistics import mean

i = int(input())
vet = list(map(int, input().split()))
print(f'{mean(vet):.2f}')

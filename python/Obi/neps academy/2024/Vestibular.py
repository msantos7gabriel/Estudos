n = int(input())
gabarito = str(input())
resposta = str(input())
r_certas = 0
for i in range(0, n):
    if gabarito[i] == resposta[i]:
        r_certas += 1
print(r_certas)
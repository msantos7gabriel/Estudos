n, saldo_inicial = map(int, input().split())
menor_valor = set()
movimentações = []

for i in range(n):
    movimentações.append(int(input()))

for i in range(n):
    if i == 0:
        menor = saldo_inicial
    saldo_inicial += movimentações[i]
    if saldo_inicial < menor:
        menor = saldo_inicial
print(menor)

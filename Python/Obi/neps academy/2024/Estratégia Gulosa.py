valor = int(input())
qtd_moedas = 0
nums = [100, 50, 25, 10, 5, 1]

for n in nums:
    if valor // n != 0:
        qtd_moedas += valor // n
        valor %= n
    elif valor == n:
        qtd_moedas += 1
        valor %= n

print(qtd_moedas)

dinheiro = int(input())
a = int(input())
f = int(input())
p = int(input())
contas = sorted([a, f, p])
c_pagas = 0
for conta in contas:
    if dinheiro - conta < 0:
        break
    else:
        dinheiro -= conta
        c_pagas += 1
print(c_pagas)
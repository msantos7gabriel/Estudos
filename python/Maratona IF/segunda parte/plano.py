quota = int(input())
n = int(input())
used_bytes = list()
saldo = 0
for _ in range(n):
    used_bytes.append(int(input()))

for ub in used_bytes:
    if ub > quota:
        saldo -= ub - quota
    else:
        saldo += abs(ub - quota)
print(quota+saldo)

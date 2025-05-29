n = int(input())
n_bin = bin(n).replace('0b', '')

for i in range(len(n_bin)):
    if n_bin[i] == '1':
        resultado = 'S'
    else:
        resultado = 'N'
        break
print(resultado)
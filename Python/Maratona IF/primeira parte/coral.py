cores = list(map(int, input().split()))
resultado = ''
i = 0
while i != 2:
    if cores[i] == cores[i+2]:
        resultado = 'V'
        break
    else:
        resultado = 'F'
    i += 1

print(resultado)

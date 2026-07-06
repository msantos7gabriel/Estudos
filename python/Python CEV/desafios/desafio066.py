n = c = s = 0
while True:
    n = int(input('Escreva um numero: (999 para parar)'))
    if n == 999:
        break
    s += n
    c += 1
print(f'Foram ditados {c} números, e sua soma é de {s}')

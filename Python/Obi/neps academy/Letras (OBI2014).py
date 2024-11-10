l = str(input())
frase = str(input()).split()

contador = 0
for f in frase:
    if l in f:
        contador += 1

porcentagem = (contador/len(frase))*100
print(f'{porcentagem:.1f}')

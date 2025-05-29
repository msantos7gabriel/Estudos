n = 0
numeros = []
instrução = []
while n != '99999':
    n = str(input())
    numeros.append(n)

for i in range(len(numeros)-1):
    if (int(numeros[i][0]) + int(numeros[i][1])) % 2 == 0 and int(numeros[i][0]) + int(numeros[i][1]) != 0:
        instrução.append(f'right {numeros[i][2:]}')
    elif (int(numeros[i][0]) + int(numeros[i][1])) % 2 != 0:
        instrução.append(f'left {numeros[i][2:]}')
    else:
        instrução.append(f'{instrução[i-1][:instrução[i-1].find(" ")]} {numeros[i][2:]}')


for i in instrução:
    print(i)

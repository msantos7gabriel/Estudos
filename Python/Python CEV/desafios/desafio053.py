frase = str(input('Escreva uma palavra: ')).strip()

frase_nova = []

for i in range(0, len(frase)):
    if frase[i] == frase[-(i + 1)]:
        palíndromo = True
    else:
        palíndromo = False
        break
for i in range(0, len(frase)):
    contador = len(frase) - 1 - i
    frase_nova.append(frase[contador])
frase_nova = "".join(frase_nova)

if palíndromo == True:
    print('{} é um palíndromo de {}' .format(frase_nova,frase))
else:
    print('{} NÃO é um palíndromo de {}' .format(frase_nova,frase))

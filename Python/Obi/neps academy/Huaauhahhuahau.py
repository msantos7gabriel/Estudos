risada = list(str(input()))
consoantes = "bcdfghjklmnpqrstvwxyz"
vogais = []
i = 0
while len(risada) != 0:
    if risada[i] not in consoantes:
        vogais.append(risada[i])
        risada.pop(0)
    else:
        for c in consoantes:
            if risada[i] == c:
                risada.pop(risada.index(c))
                break


direta = 0
esquerda = len(vogais)-1
resultado = 'S'
while direta != len(vogais):
    if vogais[direta] != vogais[esquerda]:
        resultado = 'N'
        break
    direta += 1
    esquerda -= 1

print(resultado)

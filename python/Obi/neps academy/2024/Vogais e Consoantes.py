consoantes = "bcdfghjklmnpqrstvwxyz"
vogais = "aeiou"
string = list(str(input()))

vogal = []
consoantes = []

while len(string) != 0:
    if string[0] in vogais:
        vogal.append(string[0])
        string.pop(string.index(string[0]))
    else:
        consoantes.append(string[0])
        string.pop(string.index(string[0]))

print('Vogais:', end=' ')
for v in vogal:
    print(v, end='')
print()

print('Consoantes:', end=' ')
for c in consoantes:
    print(c, end='')

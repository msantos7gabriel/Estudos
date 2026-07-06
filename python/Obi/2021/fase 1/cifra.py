from string import ascii_lowercase

palavra = str(input()).lower()
letras = ascii_lowercase
vogais = ['a', 'e', 'i', 'o', 'u']
palavra_inteira = []

for p in palavra:
    if p in vogais:
        palavra_inteira.append(p)
    else:
        id_consoante = letras.index(p)
        print(id_consoante)
def is_vogal(c):
    # Função que verifica se uma letra é uma vogal
    return c in 'aeiou'

def cifra_nlogonia(s):
    alfabeto = []
    vogais = []
    ans = []

    # Inicializando o alfabeto e as vogais
    for i in range(26):
        letra = chr(ord('a') + i) 
        if letra in ('w', 'y'):
            continue
        alfabeto.append(letra)
        if is_vogal(letra):
            vogais.append((len(alfabeto) - 1, letra))

    for char in s:
        if is_vogal(char):
            # Se a letra é uma vogal, apenas adiciona à resposta
            ans.append(char)
            continue

        # A letra atual é uma consoante
        ans.append(char)

        # Encontrar a consoante no alfabeto
        id_consoante = alfabeto.index(char)

        # Encontrar as vogais mais próximas à esquerda e à direita
        id_esquerda = -500
        id_direita = 500

        # Busca à esquerda
        for j in range(id_consoante, -1, -1):
            if is_vogal(alfabeto[j]):
                id_esquerda = j
                break

        # Busca à direita
        for j in range(id_consoante, len(alfabeto)):
            if is_vogal(alfabeto[j]):
                id_direita = j
                break

        # Comparar as distâncias das vogais e escolher a correta
        if id_consoante - id_esquerda <= id_direita - id_consoante:
            ans.append(alfabeto[id_esquerda])
        else:
            ans.append(alfabeto[id_direita])

        # Se a consoante for 'z', escolhemos ela
        # Se não, escolhemos a próxima consoante no alfabeto.
        if id_consoante == len(alfabeto) - 1:
            ans.append(char)
        else:
            for j in range(id_consoante + 1, len(alfabeto)):
                if not is_vogal(alfabeto[j]):
                    ans.append(alfabeto[j])
                    break

    # Retorna a resposta como uma string
    return ''.join(ans)

# Entrada da palavra
s = input().strip()
# Saída da palavra cifrada
print(cifra_nlogonia(s))

class Keyboard_cipher:
    def __init__(self, frase):
        self.frase = frase

    # Getter
    @property
    def frase(self):
        return self._frase

    # Setter
    @frase.setter
    def frase(self, value):
        self._frase = value.lower().strip()

    def encode(self):
        alphabet = 'qwertyuiopasdfghjklçzxcvbnm '
        encoded = []
        encoded_pairs = []
        nums = []
        for letter in self.frase:
            nums.append(alphabet.index(letter))

        for n in nums:
            if n == 27:
                encoded_pairs.append(alphabet[27])
            elif n == 0:
                encoded_pairs.append([alphabet[26]+alphabet[n+1]])
            elif n == 26:
                encoded_pairs.append([alphabet[n-1] + alphabet[0]])
            else:
                encoded_pairs.append([alphabet[n-1] + alphabet[n+1]])

        for pairs in encoded_pairs:
            for l in pairs:
                encoded.append(''.join(l))
            final = ''.join(encoded)
        print(f'Sua Frase Codificada: {final}\n')
        return final

    def decode(self):
        alphabet = ' qwertyuiopasdfghjklçzxcvbnm'
        pairs = []
        nums = []
        decoded = []
        i = 1
        try:
            while True:
                if self.frase[i-1] != ' ':
                    pairs.append([self.frase[i-1], self.frase[i]])
                    i += 2
                else:
                    pairs.append([self.frase[i-1]])
                    i += 1
        except IndexError:
            for p in pairs:
                if p[0] == ' ':
                    nums.append(0)
                elif p[0] == 'm' and p[1] == 'w':
                    nums.append(1)
                elif p[0] == 'n' and p[1] == 'q':
                    nums.append(27)
                else:
                    nums.append(
                        ((alphabet.index(p[0])+alphabet.index(p[1]))//2))
            for n in nums:
                decoded.append(alphabet[n])
        final = ''.join(decoded)
        print(f'Sua Frase Decodificada: {final}\n')
        return final

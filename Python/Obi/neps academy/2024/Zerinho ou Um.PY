def vencedor(zeros, uns):
    if zeros == 3 or uns == 3:
        return '*'
    if zeros < uns:
        indice = pessoas.index(0)
        if indice == 0:
            return 'a'
        elif indice == 1:
            return 'b'
        else:
            return 'c'
    if zeros > uns:
        indice = pessoas.index(1)
        if indice == 0:
            return 'a'
        elif indice == 1:
            return 'b'
        else:
            return 'c'


pessoas = list(map(int, input().split()))
zeros = pessoas.count(0)
uns = pessoas.count(1)

print(vencedor(zeros, uns).upper())

def leia_dinheiro(string):
    while True:
        n = str(input(f'{string}')).replace('.', ',')
        if n.isnumeric() != True:
            print(f'\033[0;31mERRO: "{n}" é um preço inválido!\033[m')
        else:
            return float(n)

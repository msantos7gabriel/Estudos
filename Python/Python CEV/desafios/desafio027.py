nome = str(input('Qual Seu Nome: '))
nome = nome.split()
print("Primeiro nome: {}\n Ultimo nome: {}".format(
    nome[0], nome[-1]))  # Ou nome[len(nome)-1]

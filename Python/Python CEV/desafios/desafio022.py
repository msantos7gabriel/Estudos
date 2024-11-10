from re import split

nome = str(input("Qual é o seu nome: "))

print("Nome todo em Maiúsculo: {}".format(nome.upper()))
print("Nome todo em Minusculo: {}".format(nome.lower()))
print("Quantidade de caracteres (sem os espaços): {}".format(len(nome.strip())))
primeiro_nome = nome.split()
print("Quantidade de caracteres no primeiro nome: {}".format(
    len(primeiro_nome[0])))

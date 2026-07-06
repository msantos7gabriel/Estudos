flag = ''
media = 0
n = 0
maior = 0
menor = 100000

while flag != 'N':
    num = int(input("Escreva um numero: "))
    media += num
    n += 1
    if menor > num:
        menor = num
    if maior < num:
        maior = num

    while flag != 'S' or flag != 'N':
        flag = str(input("Deseja Continuar ? [S/N] ")).upper()
        if flag != 'S' and flag != 'N':
            print("Caractere Invalido !")
        else:
            break

media = media / n
print('Foi digitado {} Números\nA media entre todos os valores foi: {:.2f}'.format(n, media))
print('O Menor numero foi: {} e o Maior foi: {}'.format(menor, maior))

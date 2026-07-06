import math

n1 = int(input('Escreva um número: '))
dobro = n1 * 2
triplo = n1 * 3
sqrt = math.sqrt(n1)
print('Seu Dobro é: {}\nSeu Triplo é: {} \n Sua Raiz Quadrada é: {}'.format(
    dobro, triplo, round(sqrt, 2))) # ou {:.2f}

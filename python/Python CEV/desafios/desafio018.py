import math
angulo = float(input('Escreva o Angulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('O Angulo: {}\n tem seu Seno de: {:.2f},\n Seu Cosseno de: {:.2f},\n e Sua Tangente: {:.2f}'.format(
    angulo, seno, cosseno, tangente))

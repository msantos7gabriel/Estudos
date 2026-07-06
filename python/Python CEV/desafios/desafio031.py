dist= int(input('Qual a Distancia da Viagem em Km: '))
if dist <= 200:
    dist*= 0.5
else:
    dist*= 0.45
print('O valor total da viagem é: {}'.format(dist))
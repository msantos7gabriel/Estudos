peso = []
maior = 0
menor = 0
for i in range(0, 5):
    peso.append(float(input('Insira seu peso: ')))

for i in range(0, 5):
    if peso[i] > maior:
        maior = peso[i]
    if menor > peso[i] or menor == 0:
        menor = peso[i]

print('O maior peso é: {}Kg, e O menor peso é: {}Kg '.format(maior, menor))

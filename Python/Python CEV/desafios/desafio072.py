extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
           'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
           'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze',
           'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    numero = (int(input("Digite Um número entre 0 e 20: ")))
    if 20 >= numero >= 0:
        break
    print('Tente Novamente.', end=' ')
print(f'Você Digitou o número {extenso[numero]}')

preco_normal = float(input('Escreva o valor a ser Pago: '))
metodo = int(input(
    'Qual o método de pagamento: \n\n1. Avista\n2. Á vista no Cartão\n3. 2x no cartão\n4. 3x ou no cartão\n'))

if metodo == 1:
    preco_normal *= 0.9
elif metodo == 2:
    preco_normal *= 0.95
elif metodo == 3:
    preco_normal *= 1
elif metodo == 4:
    preco_normal *= 1.20

print('O valor final é de: {}'.format(preco_normal))

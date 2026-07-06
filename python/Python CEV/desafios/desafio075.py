valores = (int(input('Digite um numero: ')),
           int(input('Digite um numero: ')),
           int(input('Digite um numero: ')),
           int(input('Digite um numero: ')))

print(f'Você digitou os valores {valores}')
print(f'O valor 9 apareceu {valores.count(9)} vezes')

if 3 in valores:
    print(f'O valor 3 apareceu na {valores.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os números pares digitados foram', end=' ')
for i in range(0, len(valores)):
    if valores[i] % 2 == 0:
        print(valores[i], end=' ')

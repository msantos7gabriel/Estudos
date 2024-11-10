produto_nome = []
produto_preço = []
while True:
    print('-'*30)
    print(f'{'LOJA SUPER BARATÃO':^30}')
    print('-'*30)
    nome = str(input('Nome do Produto: '))
    preço = float(input('Preço R$'))
    produto_nome.append(nome)
    produto_preço.append(preço)
    while True:
        continuar = str(
            input('\nDeseja continuar? [S/N]: ')).strip().upper()[0]
        if continuar in 'SN':
            break
        print('Escreva um valor valido!')
    print('-'*30)
    if continuar == 'N':
        print(f'{'Fim do Programa':_^40}')
        break

n = soma = menor_id = count = 0
menor = produto_preço[0]
while len(produto_preço) > n:
    soma += produto_preço[n]
    if produto_preço[n] < menor:
        menor_id = n
    if produto_preço[n] > 1000:
        count += 1
    n += 1

print(f'Total da compra foi: R${soma:.2f}')
print(f'Temos {count} produtos custando mais de R$1000.00')
print('o produto mais barato foi {} que custa R${:.2f}'.format(
    produto_nome[menor_id], produto_preço[menor_id]))

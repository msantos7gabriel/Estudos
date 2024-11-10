teste = []
galera = []
teste.append('Gustavo')
teste.append(40)
galera.append(teste[:])  # Pega a copia da variável Teste
# galera.append(teste) # Faz a ligação com a variável (caso a variável mude a lista tb vai mudar)
print(galera)
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

galera = [['João', 20], ['Ana', 33], ['José', 33], ['Maria', 25]]
for p in galera:
    print(f'{p[0]} tem {p[1]} de idade.')

galera = []
dado = []

totmaior = totmenor = 0

for i in range(0, 3):
    dado.append(str(input('\nNome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)


for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmenor += 1
print(f'\nTotal de maiores de idade {
      totmaior}\n Total de menores de idade {totmenor}')

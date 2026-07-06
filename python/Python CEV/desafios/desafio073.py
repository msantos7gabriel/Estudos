times_classificacao = ("Fortaleza", "Botafogo", "Palmeiras", "Flamengo", "São Paulo", "Bahia", "Cruzeiro", "Athletico-PR", "Atlético-MG",
                       "Vasco da Gama", "Internacional", "Juventude", "Grêmio", "Bragantino", "Criciúma", "Fluminense", "EC Vitória",
                       "Corinthians", "Cuiabá", "Atlético-GO",)


print('-='*15)
print(f'Lista de Times do Brasileirão: {times_classificacao}')
print('-='*15)
print(f'Os 5 Primeiros Times: {times_classificacao[:6]}')
print('-='*15)
print(f'Os 4 Últimos Times: {times_classificacao[-4:]}')
print('-='*15)
print(f' Times em Ordem alfabética: {sorted(times_classificacao)}')
print('-='*15)
for i in range(0, len(times_classificacao)):
    if times_classificacao[i] == 'Cruzeiro':
        print(f'O Cruzeiro Está em {i}ª posição')
        break

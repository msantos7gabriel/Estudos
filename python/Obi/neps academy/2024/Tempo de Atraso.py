hora_atual = int(input())
minuto_atual = int(input()) + 45
hora_reunião = int(input())
minuto_reunião = int(input())

if minuto_atual >= 60:
    hora_atual += minuto_atual // 60
    minuto_atual %= 60

if hora_atual < hora_reunião or (hora_atual == hora_reunião and minuto_atual <= minuto_reunião):
    print('Sucesso')
else:
    atraso_minutos = (hora_atual - hora_reunião) * 60 + (minuto_atual - minuto_reunião)
    print(f'Atrasado {atraso_minutos}')

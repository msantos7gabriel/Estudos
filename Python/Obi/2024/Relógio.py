horas = int(input())
minutos = int(input())
segundos = int(input())
segundos_adiados = int(input())

segundos += segundos_adiados
minutos += segundos // 60
segundos %= 60
horas += minutos // 60
minutos %= 60
if horas >= 24:
    horas = horas % 24

print(horas)
print(minutos)
print(segundos)

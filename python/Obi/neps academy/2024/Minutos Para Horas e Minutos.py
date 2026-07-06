from math import trunc

m = int(input())
horas = trunc(m / 60) 
minutos = m%60
print(horas)
print(minutos)
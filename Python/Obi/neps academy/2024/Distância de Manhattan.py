distancias = list(map(int, input().split()))
Xm, Ym, Xr, Yr = distancias
distancia_manhattan = abs(Xm - Xr) + abs(Ym - Yr)
print(distancia_manhattan)

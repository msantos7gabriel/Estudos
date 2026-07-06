m = float(input('Escreva Um valor em Metros: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print(
    'Valor Convertido em centímetros: {:.0f} Valor Convertido em milímetros: {:.0f}'.format(cm, mm))

print('Quilômetros: {}'.format(km))
print('Hectômetros: {}'.format(hm))
print('Decâmetro: {}'.format(dam))
print('Metros: {}'.format(m))
print('Decímetros: {}'.format(dm))
print('Centímetros: {}'.format(cm))
print('Milímetros: {}'.format(mm))

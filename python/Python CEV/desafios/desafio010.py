reais = float(input('Quanto Dinheiro você tem na carteira: R$'))
dolar = reais / 5.35
euro = reais / 5.77
print('Você Pode compra US${:.2f}'.format(dolar))
print('ou Você Pode compra EU${:.2f}'.format(euro))

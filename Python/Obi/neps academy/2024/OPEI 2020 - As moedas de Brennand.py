import sys
valor = []

for linha in sys.stdin:
    print(linha)
    valor.append(int(linha.strip()))
valor.sort()
print(f"Apesar de muitas moedinhas o maior produto encontrado foi {valor[-1]*valor[-2]}")


import math

# Função otimizada para verificar se um número é primo
def eh_primo(x):
    if x <= 1:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    limite = int(math.sqrt(x)) + 1
    for i in range(3, limite, 2):  # Testa apenas números ímpares
        if x % i == 0:
            return False
    return True

# Entrada do número
x = int(input())
primos = []

# Loop otimizado para buscar os primos em ordem decrescente
for i in range(x, 1, -1):
    if eh_primo(i):
        primos.append(i)

# Exibe os números primos encontrados
primos.sort()
print(*primos)

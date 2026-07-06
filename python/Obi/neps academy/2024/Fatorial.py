# Usando função da math
# from math import factorial
# n1 = int(input(''))
# print(factorial(n1))

# Fazendo no "Braço"
n1 = int(input(''))
if n1 == 0:
    print(1)
else:
    for i in range(1, n1):
        n1 *= i
    print(n1)

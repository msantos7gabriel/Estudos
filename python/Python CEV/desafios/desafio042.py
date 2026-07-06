a = float(input("Digite o comprimento da primeira reta: "))
b = float(input("Digite o comprimento da segunda reta: "))
c = float(input("Digite o comprimento da terceira reta: "))

if a + b > c and a + c > b and b + c > a:
    print("As retas podem formar um triângulo.")
else:
    print("As retas não podem formar um triângulo.")


if a == b and a == c and b == c:
    print('Triângulo Equilátero')
elif a != b and a != c and b != c:
    print('Triângulo Escaleno')
else:
    print('Triângulo Equilátero')

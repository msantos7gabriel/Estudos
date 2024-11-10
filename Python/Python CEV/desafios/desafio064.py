num = 0
num1 = 0
n = 0

while num != 999:
    num = int(input("Digite um número: "))
    num1 += num
    n += 1

print("Foram digitados {} e a Soma entre eles é: {}".format(n-1, num1 - 999))

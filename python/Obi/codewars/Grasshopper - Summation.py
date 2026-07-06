def summation(num):
    soma = 0   
    for i in range(1, num+1):
        soma += i
    return soma

print(summation(8))
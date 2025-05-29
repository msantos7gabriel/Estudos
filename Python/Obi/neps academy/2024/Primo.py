def eh_primo(x):
    if x <= 1:
        return False
    contador = 0
    for i in range(1, x+1):
        if x % i == 0:
            contador += 1
            if contador > 2:
                return False
    return True
    

x = int(input())

if eh_primo(x):
    print("S")
else:
    print("N")

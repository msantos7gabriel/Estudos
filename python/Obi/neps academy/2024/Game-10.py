n_posições = int(input())
pos_disco = int(input())
pos_aviao = int(input())
i = 0
while True:
    if pos_disco != pos_aviao:
        pos_aviao += 1
        i += 1
        if pos_aviao > n_posições:
            pos_aviao = 1
    else:
        break
print(i)
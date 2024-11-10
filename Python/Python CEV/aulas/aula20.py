def soma(*nums):
    print(sum(nums))


soma(10, 12, 2, 90, 1)


def dobra(list):
    for i in range(len(list)):
        list[i] *= 2


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)

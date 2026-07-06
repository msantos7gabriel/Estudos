placa = list(str(input()))


def brasil():
    for i in range(3):
        if not placa[i].isalpha():
            return 0

    if placa[3] == '-':
        for i in range(4, len(placa)):
            if not placa[i].isnumeric():
                return 0
    else:
        return 0


def mecor_sul():
    for i in range(2):
        if not placa[i].isalpha():
            return 0
    for i in range(3, len(placa)):
        if i % 2 != 0:
            if not placa[i].isnumeric():
                return 0
        else:
            if not placa[4].isalpha():
                return 0
    return 2


if len(placa) > 8 or len(placa) < 7:
    print(0)
else:
    if brasil() == 0:
        if mecor_sul() == 0:
            print(0)
        else:
            print(2)
    else:
        print(1)

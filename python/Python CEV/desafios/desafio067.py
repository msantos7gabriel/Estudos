n = 0
c = 1
while True:
    n = int(input('Quer ver a tabuada de qual valor?: '))
    if n < 0:
        break
    print('-'*30)
    while c <= 10:
        print(f'{n} x {c} = {n*c}')
        c += 1
    print('-'*30)
    c = 1

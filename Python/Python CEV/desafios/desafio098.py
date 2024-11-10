from time import sleep


def contador(i, f, p=1):
    print('-='*20)
    if p == 0:
        p = 1
    if p < 0:
        print(f'Contagem de {i} ate {f} de {p*-1} em {p*-1}')
    else:
        print(f'Contagem de {i} ate {f} de {p} em {p}')
        sleep(2.5)

    if f != 0 and f > 0:
        f += 1
    elif f < 0:
        f -= 1
    if i > f:
        p *= -1
        if f == 0:
            f -= 1

    for j in range(i, f, p):
        print(j, end=' ', flush=True)
        # flush = buffer de tela
        sleep(0.5)
    print('Fim!')


contador(1, 10)
contador(10, 0, 2)
print('-='*20)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)

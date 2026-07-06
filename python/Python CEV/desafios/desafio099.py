from time import sleep


def maior(*num):
    print('-='*30)
    print('Analisando os valores passados...')
    for n in num:
        print(n, end=' ', flush=True)
        sleep(0.5)
    print(f'Foram informados {len(num)} valores ao todo.')
    if len(num) == 0:
        m = 0
    else:
        m = max(num)
    print(f'O Maior valor informado foi {m}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)
maior()

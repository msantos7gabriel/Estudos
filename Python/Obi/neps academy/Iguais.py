n_pilhas = int(input())
monte = list(map(int, input().split()))
pedras = int(input())

while pedras != 0:
    for i in range(0, n_pilhas):
        if pedras == 0:
            break
        try:
            while True:
                if monte[i] < monte[i+1] or monte[i] < monte[i-1] and pedras > 0:
                    monte[i] += 1
                    pedras -= 1
                else:
                    break
        except:
            if i == 0:
                while True:
                    if monte[i] < monte[i+1] and pedras > 0:
                        monte[i] += 1
                        pedras -= 1
                    else:
                        break
            else:
                while True:
                    if monte[i] < monte[i-1] and pedras > 0:
                        monte[i] += 1
                        pedras -= 1
                    else:
                        break

if len(set(monte)) == 1:
    print("Boa Sorte")
else:
    print("Sem Sorte")


# https://neps.academy/br/exercise/1469
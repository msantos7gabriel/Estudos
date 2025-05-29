cartas = []
for i in range(3):
    cartas.append(int(input()))
for c in cartas:
    if cartas.count(c) ==1:
        print(c)
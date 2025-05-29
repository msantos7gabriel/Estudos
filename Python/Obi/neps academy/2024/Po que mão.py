doces = int(input())
Pokemon = list()
evoluções = 0

for i in range(3):
    Pokemon.append(int(input()))
Pokemon.sort()

for p in Pokemon:
    if doces - p >= 0:
        doces -= p
        evoluções += 1

print(evoluções)

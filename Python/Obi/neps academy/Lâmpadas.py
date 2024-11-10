def is_ligado(nums):
    if nums == 1:
        return True
    else:
        return False


def inversor(nums):
    if nums == 1:
        return 0
    else:
        return 1


n = int(input())
n1 = n2 = 0
list = list(map(int, input().split()))
for num in list:
    if num == 1:
        if is_ligado(n1):
            n1 = 0
        else:
            n1 = 1
    else:
        n1 = inversor(n1)
        n2 = inversor(n2)
print(n1)
print(n2)

n = int(input())
nums = []
campo_minado = []
for i in range(0, n):
    nums.append(int(input()))
for j in range(0, len(nums)):
    bombas = 0
    if len(nums) == 1:
        if nums[j] == 1:
            bombas += 1
    elif j == 0:
        if nums[j] == 1:
            bombas += 1
        if nums[j+1] == 1:
            bombas += 1
    elif j == len(nums)-1:
        if nums[j] == 1:
            bombas += 1
        if nums[j-1] == 1:
            bombas += 1
    else:
        if nums[j-1] == 1:
            bombas += 1
        if nums[j] == 1:
            bombas += 1
        if nums[j+1] == 1:
            bombas += 1
    campo_minado.append(bombas)
for cp in campo_minado:
    print(cp, end='')

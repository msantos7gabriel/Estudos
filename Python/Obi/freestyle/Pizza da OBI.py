pessoas = int(input())
pizza_8 = int(input())
pizza_6 = int(input())

total_pedaços = (pizza_8 * 8) + (pizza_6 * 6)

if total_pedaços > pessoas:
    print(total_pedaços - pessoas) 
else:
    print('0')
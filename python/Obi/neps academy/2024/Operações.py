opr = str(input())
nums = list(map(float, input().split()))

if opr == 'M':
    print(f'{nums[0]*nums[1]:.2f}')
else:
    print(f'{nums[0]/nums[1]:.2f}')
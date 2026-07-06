def limiter_verification(opr, limiter):
    if opr > limiter:
        print('OVERFLOW')
    else:
        print('OK')

limiter = int(input())
exprs = list(map(str, input().split()))

if exprs[1] == '+':
    opr = int(exprs[0])+int(exprs[2])
    limiter_verification(opr, limiter)
else:
    opr = int(exprs[0])*int(exprs[2])
    limiter_verification(opr, limiter)

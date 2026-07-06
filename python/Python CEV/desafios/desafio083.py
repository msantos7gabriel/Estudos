expre = str(input('Digite a expressão: '))
count0 = count1 = 0

for i in range(0, len(expre)):
    if expre[i] == '(':
        count0 += 1
    if expre[i] == ')':
        count1 += 1

if count1 == count0:
    print('Sua está Correta!')
else:
    print('Sua está errada!')

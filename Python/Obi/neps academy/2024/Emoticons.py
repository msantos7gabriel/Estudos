frase = str(input()) 
d = frase.count(':-)')
c = frase.count(':-(')

if d > c :
    print('divertido')
elif c> d :
    print('chateado')
else:
    print('neutro')

sexo = ''
while sexo != 'F' and sexo != 'M':
    sexo = str(input("Qual seu sexo [M/F]: ")).upper()
    if sexo != 'F' and sexo != 'M':
        print('\nPor Favor insira corretamente\n')
print("Sexo {} Registrado".format(sexo))

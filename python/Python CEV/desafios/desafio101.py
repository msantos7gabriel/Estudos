def voto(idade):
    from datetime import date
    hj = date.today().year
    idade = hj - nascimento
    if 18 <= idade <= 70:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    elif 16 >= idade < 18 or idade > 70:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO NEGADO.'


print('-'*30)
nascimento = int(input('Em quem ano você nasceu? '))
print(voto(nascimento))

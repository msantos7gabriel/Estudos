try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou')
except ZeroDivisionError:
    print('Não é possível dividir um numero por zero!')
except KeyboardInterrupt:
    print('O Usuário preferiu não informar os dados!')
except Exception as error:
    print(f'O erro encontrado foi {error.__class__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')

# Else e Finally são opcionais

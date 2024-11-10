# Classes 

from pessoa import Pessoa

p1 = Pessoa('Luiz', 29)
p2 = Pessoa('João', 32)

p1.falar('POO')
p2.comer('Sorvete')
p1.parar_falar()
p1.comer('Churrasco')

print(f'\n{p1.nome} Nasceu em {p1.get_ano_nascimento()}')
print(f'{p2.nome} Nasceu em {p2.get_ano_nascimento()}')

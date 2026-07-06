# Métodos estáticos

from datetime import datetime
from random import randint


class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod
    def gera_id():
        rand = randint(10_000, 19_999)
        return rand


p1 = Pessoa.por_ano_nascimento('Gabriel', 2007)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()
print(p1.gera_id())

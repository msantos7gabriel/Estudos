from datetime import datetime


class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def falar(self, assunto='abobrinha'):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo')
        elif self.falando:
            print(f'{self.nome} já está falando')
        else:
            print(f'{self.nome} está falando sobre {assunto}')
            self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando')
        else:
            print(f'{self.nome} parou de falar')
            self.falando = False

    def comer(self, alimento='Maçã'):
        if self.comendo:
            print(f'{self.nome} já está comendo')
        elif self.falando:
            print(f'{self.nome} não pode comer falando')
        else:
            print(f'{self.nome} está comendo {alimento}.')
            self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo!')
        else:
            self.comendo = False
            print(f'{self.nome} parou de comer')

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade

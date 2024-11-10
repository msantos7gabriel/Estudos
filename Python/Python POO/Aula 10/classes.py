class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
        self.Nome_Classe = self.__class__.__name__

    def falar(self):
        print(f'{self.Nome_Classe} Falando...')


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.Nome_Classe} Comprando...')


class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.Nome_Classe} Estudando...')

# @property - Getters e Setters 

class Produto:

    def __init__(self, nome, preço):
        self.nome = nome
        self.preço = preço

    def desconto(self, percentual):
        self.preço = round(self.preço - (self.preço * (percentual/100)), 2)

    # Getter

    @property
    def preço(self):
        return self._preço

    @property
    def nome(self):
        return self._nome

    # Setter

    @preço.setter
    def preço(self, valor):
        if isinstance(valor, str):
            valor = float(valor.lower().replace('r$', ''))
        self._preço = valor

    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()


p1 = Produto('Camiseta', 50)
p1.desconto(10)
print(p1.nome, p1.preço)

p2 = Produto('Caneca', 'R$15')
p2.desconto(10)
print(p2.nome, p2.preço)

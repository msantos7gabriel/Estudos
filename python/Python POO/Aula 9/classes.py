class Cliente:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
        self.endereços = list()

    def insere_endereço(self, cidade, estado):
        self.endereços.append(Endereço(cidade, estado))

    def lista_endereços(self):
        for endereço in self.endereços:
            print(endereço.cidade, endereço.estado)

    def __del__(self):
        print(f'{self.nome} FOI APAGADO')


class Endereço:
    def __init__(self, cidade, estado) -> None:
        self.cidade = cidade
        self.estado = estado

    def __del__(self):
        print(f'{self.cidade}/{self.estado} FOI APAGADO\n')

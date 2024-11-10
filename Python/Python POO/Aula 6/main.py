# Encapsulamento

"""
Public, Protected, Private
'_' Privado / Protected (public _)
'__' Privado (_NOMECLASSE__nomeatributo) 
"""


class BaseDeDados:
    def __init__(self):
        self.__dados = dict()

    @property
    def dados(self):
        return self.__dados

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(f'Id: {id}, Cliente: {nome}')

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]


bd = BaseDeDados()
bd.inserir_cliente(1, 'Otávio')
bd.inserir_cliente(2, 'Rose')
print(bd.dados)

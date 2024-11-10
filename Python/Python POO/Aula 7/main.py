# Associação

from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever

e1 = Escritor('José')
c1 = Caneta('Bic')
m1 = MaquinaDeEscrever()

e1.ferramenta = m1
e1.ferramenta.escrever()

del e1
print(c1.marca)
m1.escrever()
c1.escrever()
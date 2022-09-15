"""
    Suponga que es el administrador de un zoológico, el cual debe matener diferentes tipos de animales 
    (Gorilas y Conejos), tenga en cuenta que un animal consta de peso y altura y que a cada animal se le 
    debe proporcionar uno o varios alimentos a consumir; también para cada animal se debe calcular su IMC; 
    Por último, a un conejo se le debe proporcionar un 
    diente principal y al gorila se le debe calcular el peso total de los alimento ya que puede consumir 
    varios de ellos.
"""
from animales.Conejo import Conejo
from animales.Gorila import Gorila

conejo = Conejo(3, 0.2, ["hierba", "agua"], "colmillo")
print(conejo.get_peso())
print(conejo.get_altura())
print(conejo.get_IMC())
print(conejo.get_alimentos())

gorila = Gorila(80, 1.20, ["banana", "pera", "hierba"])
print(gorila.get_peso())
print(gorila.get_altura())
print(gorila.get_IMC())
print(gorila.get_alimentos())

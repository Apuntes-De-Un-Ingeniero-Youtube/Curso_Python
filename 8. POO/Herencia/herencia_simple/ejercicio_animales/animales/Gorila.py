from animales.Animal import Animal


class Gorila(Animal):

    # Constructor
    def __init__(self, peso, altura, alimentos):
        super().__init__(peso, altura, alimentos)

    def comer(self):
        lista = []
        for i in self._alimentos:
            lista.append(f"\nComiendo: {i}")
        return lista

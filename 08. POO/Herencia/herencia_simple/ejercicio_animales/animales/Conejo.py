from animales.Animal import Animal


class Conejo(Animal):

    # Constructor
    def __init__(self, peso, altura, alimentos, diente):
        super().__init__(peso, altura, alimentos)
        self._diente = diente

    # ---- Get y Set ----
    def set_diente(self, diente):
        self.__diente = diente

    def get_diente(self):
        return self.__diente
    # ---- Fin Get y Set ----

class Animal:

    # Método constructor OPTIONAL

    def __init__(self, peso, altura, alimentos):
        self._peso = peso
        self._altura = altura
        self._alimentos = alimentos

    # ---- Get y Set ----
    def set_peso(self, peso):
        self._peso = peso

    def get_peso(self):
        return self._peso

    def set_altura(self, altura):
        self._altura = altura

    def get_altura(self):
        return self._altura

    def set_alimentos(self, alimentos):
        self._alimentos = alimentos

    def get_alimentos(self):
        return self._alimentos
    # ---- Fin Get y Set ----

    # Se encarga de calcular el IMC de un animal
    def get_IMC(self):
        return ((self._peso) / (self._altura * self._altura))
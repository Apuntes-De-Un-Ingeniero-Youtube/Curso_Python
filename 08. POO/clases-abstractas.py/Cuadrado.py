from FiguraGeometrica import FiguraGeometrica


class Cuadrado(FiguraGeometrica):

    # Constructor
    def __init__(self, ancho, alto):
        FiguraGeometrica.__init__(self, ancho, alto)

    # Implementando el método abstracto de la clase FiguraGeometrica

    def calcular_area(self):
        return self._alto * self._ancho

    def __str__(self) -> str:
        return f"{FiguraGeometrica.__str__(self)}"

from FiguraGeometrica import FiguraGeometrica


class Triangulo(FiguraGeometrica):

    def __init__(self, ancho, alto):
        FiguraGeometrica.__init__(self, ancho, alto)

    # Implementando el método abstracto de la clase FiguraGeometrica

    def calcular_area(self):
        return (self._alto * self._ancho) / 2

    def __str__(self) -> str:
        return f"{FiguraGeometrica.__str__(self)}"

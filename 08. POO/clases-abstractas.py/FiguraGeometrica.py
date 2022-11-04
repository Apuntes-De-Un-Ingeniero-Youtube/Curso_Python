from abc import ABC, abstractmethod

# Clase abstracta para todo tipo de figura geométrica


class FiguraGeometrica(ABC):

    # Constructor de clase
    def __init__(self, ancho, alto):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            self._ancho = 0
            print("Error, el ancho de la figura no puede ser negativo")

        if self._validar_valor(alto):
            self._alto = alto
        else:
            self._alto = 0
            print("Error, el alto de la figura no puede ser negativo")

    # --- Get y Set ---
    def set_ancho(self, ancho):
        self._ancho = ancho

    def get_ancho(self):
        return self._ancho

    def set_alto(self, alto):
        self._alto = alto

    def get_alto(self):
        return self._alto
    # --- Fin Get y Set ---

    # Valida que un valor específico sea positivo
    def _validar_valor(self, valor):
        return True if valor >= 0 else False

    @abstractmethod
    def calcular_area(self):
        pass

    def __str__(self) -> str:
        return f"Figura Geométrica [Ancho: {self._ancho}, Alto: {self._alto}]"

"""
    Definir una clase padre llamada Vehiculo y dos clases hijas llamadas Coche y Bicicleta,
    las cuales heredan de la clase Padre Vehiculo.
    La clase padre debe tener los siguientes atributos y métodos

    Vehiculo (Clase Padre):
    -Atributos (color, ruedas)
    -Métodos ( __init__() y __str__ )

    Coche  (Clase Hija de Vehículo) (Además de los atributos y métodos heradados de Vehículo):
    -Atributos ( velocidad (km/hr) )
    -Métodos ( __init__() y __str__() )

    Bicicleta  (Clase Hija de Vehículo) (Además de los atributos y métodos heradados de Vehículo):
    -Atributos ( tipo (urbana/montaña/etc )
    -Métodos ( __init__() y __str__() )
"""


class Vehiculo:

    # Constructor
    def __init__(self, color, ruedas):
        self._color = color
        self._ruedas = ruedas

    def __str__(self):
        return f"Color: {self._color}, Ruedas: {str(self._ruedas)}"


class Coche(Vehiculo):

    # Constructor
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self._velocidad = velocidad

    def __str__(self):
        return f"{super().__str__()}, Velocidad(km/h): {str(self._velocidad)}"


class Bicicleta(Vehiculo):

    # Constructor
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self._tipo = tipo

    def __str__(self):
        return super().__str__() + ", Tipo: " + self._tipo


vehiculo1 = Vehiculo("Rojo", 4)
print(vehiculo1)

ferrari = Coche("Amarillo", 4, 245)
print(ferrari)

biciBacana = Bicicleta("Azul", 2, "Montaña")
print(biciBacana)

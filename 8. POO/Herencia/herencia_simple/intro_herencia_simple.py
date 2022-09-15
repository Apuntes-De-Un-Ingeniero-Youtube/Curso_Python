class Padre:

    # Constructor de clase
    def __init__(self, nombre, apellido, carro):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__carro = carro

    def jugar_futbol(self):
        return "Jugando futbol"

    def cocinar(self):
        return "cocinando"

    def __str__(self):
        return f"Datos básicos Padre: \nNombre: {self.__nombre}\nApellido: {self.__apellido} \nCarro: {self.__carro}"


class Hijo(Padre):

    # Constructor de clase
    def __init__(self, nombre, apellido, carro, motocicleta):
        super().__init__(nombre, apellido, carro)
        self.__motocicleta = motocicleta

    def correr(self):
        return "corriendo"


padre = Padre("Juan", "Estevez", "SI")
print(padre.__str__())
print(padre.jugar_futbol())
print(padre.cocinar())
print("\n----------------------\n")
hijo = Hijo("Pedro", "Jimenez", "Si", "Si")
print(hijo.jugar_futbol())
print(hijo.cocinar())
print(hijo.correr())

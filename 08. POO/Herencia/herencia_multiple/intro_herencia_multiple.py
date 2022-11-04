class Madre:

    # Constructor de clase
    def __init__(self, nombre, apellido, lote):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__lote = lote

    def get_lote(self):
        return "Lote:", self.__lote

    def jugar_volei(self):
        return "jugando volei"

    def ayudar(self):
        return "ayudando a las personas"

    def __str__(self):
        return f"Datos básicos Madre: \nNombre: {self.__nombre}\nApellido: {self.__apellido} \nLote: {self.__lote}"


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

    def get_carro(self):
        return "Carro:", self.__carro

    def __str__(self):
        return f"Datos básicos Padre: \nNombre: {self.__nombre}\nApellido: {self.__apellido} \nCarro: {self.__carro}"


class Hijo(Padre, Madre):

    # Constructor de clase
    def __init__(self, nombre, apellido, carro, lote):
        Padre.__init__(self, nombre, apellido, carro)
        Madre.__init__(self, nombre, apellido, lote)

    def correr(self):
        return "corriendo"


class Nieto(Hijo):

    # Constructor de clase
    def __init__(self, nombre, apellido, carro, lote):
        super().__init__(nombre, apellido, carro, lote)

    # Podria tener sus propios metodos y campos de clase.


madre = Madre("Laura", "Perez", "SI")
print(madre.__str__())
print(madre.ayudar())
print(madre.jugar_volei())
print("\n----------------------\n")

padre = Padre("Juan", "Estevez", "SI")
print(padre.__str__())
print(padre.jugar_futbol())
print(padre.cocinar())
print("\n----------------------\n")

hijo = Hijo("Pedro", "Jimenez", "Si", "Si")
print(hijo.jugar_futbol())
print(hijo.cocinar())
print(hijo.correr())
print(hijo.jugar_volei())
print(hijo.ayudar())
print(hijo.get_carro())
print(hijo.get_lote())

print("\n----------------------\n")

nieto = Nieto("Pedro", "Jimenez", "Si", "Si")
print(nieto.jugar_futbol())
print(nieto.cocinar())
print(nieto.correr())
print(nieto.jugar_volei())
print(nieto.ayudar())
print(nieto.get_carro())
print(nieto.get_lote())

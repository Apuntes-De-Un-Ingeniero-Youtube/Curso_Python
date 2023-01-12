class Cliente:

    def __init__(self, *args):
        if len(args) == 0:
            self.__nombre = ""
            self.__apellido = ""
            self.__email = ""
            self.__razon_social = ""
            self.__telefono = 0

        if len(args) == 5:
            self.__nombre = args[0]
            self.__apellido = args[1]
            self.__email = args[2]
            self.__razon_social = args[3]
            self.__telefono = args[4]

        if len(args) == 6:
            self.__id_cliente = args[0]
            self.__nombre = args[1]
            self.__apellido = args[2]
            self.__email = args[3]
            self.__razon_social = args[4]
            self.__telefono = args[5]

    def get_id_cliente(self):
        return self.__id_cliente

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

    def set_apellido(self, apellido):
        self.__apellido = apellido

    def get_apellido(self):
        return self.__apellido

    def set_email(self, email):
        self.__email = email

    def get_email(self):
        return self.__email

    def set_razon_social(self, razon_social):
        self.__razon_social = razon_social

    def get_razon_social(self):
        return self.__razon_social

    def set_telefono(self, telefono):
        self.__telefono = telefono

    def get_telefono(self):
        return self.__telefono

    def __str__(self):
        return f"""\n\n--- Cliente N° {self.get_id_cliente()}---
    Nombre: {self.get_nombre()}
    Apellido: {self.get_apellido()}
    Email: {self.get_email()}
    Razón Social: {self.get_razon_social()}
    Teléfono: {self.get_telefono()}
    """

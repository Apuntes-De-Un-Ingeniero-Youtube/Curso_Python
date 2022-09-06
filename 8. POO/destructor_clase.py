class Celular:  # Molde principal

    def __init__(self):
        self.__pantalla = ""
        self.__forma = ""
        self.__ram = 0
        self.__almacenamiento = 0
        self.__camara = 0

    def get_pantalla(self):
        return self.__pantalla

    def set_pantalla(self, pantalla):
        self.__pantalla = pantalla

    def get_forma(self):
        return self.__forma

    def set_forma(self, forma):
        self.__forma = forma

    def get_ram(self):
        return self.__ram

    def set_ram(self, ram):
        self.__ram = ram

    def get_almacenamient(self):
        return self.__almacenamiento

    def set_almacenamiento(self, almacenamiento):
        self.__almacenamiento = almacenamiento

    def get_camara(self):
        return self.__camara

    def set_camara(self, camara):
        self.__camara = camara

    def __del__(self):
        print(f'Celular: {self.__almacenamiento} {self.__camara}')
    
print("Creando un objeto de tipo celular") # memoria 65787A
celular = Celular()
celular.set_almacenamiento(256)
celular.set_camara(8)
celular.set_forma("curva")
celular.set_pantalla("amoled")
print(celular) # Celular nuevo qu apunta a una dirección de memoria.
del celular # Eliminando el celular de arriba con la dirección 65787A
celular2 = Celular()
celular2.set_almacenamiento(252)
celular2.set_camara(84)
celular2.set_forma("curva")
celular2.set_pantalla("amoled 2")
print(celular2)


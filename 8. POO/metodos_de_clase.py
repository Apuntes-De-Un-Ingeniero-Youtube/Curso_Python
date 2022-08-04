class Celular:  # Molde principal

    # Constructor de clase
    def __init__(self):
        self.__pantalla = ""
        self.__forma = ""
        self.__ram = 0
        self.__almacenamiento = 0
        self.__camara = 0
        self.__encendido = False

    # Métodos Getter and Setter
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

    def get_encendido(self):
        return self.__encendido

    # Métodos de clase
    def encender(self):
        print("Encendiendo Celular")
        self.__encendido = True

    def apagar(self):
        print("Apagando ...")
        self.__encendido = False

    # Método toString
    def __str__(self):
        return f'\nImprimiendo datos del celular desde el método ToString\nPantalla -> {samsung.__pantalla}\nAlmacenamiento -> {samsung.__almacenamiento}'


samsung = Celular()  # Celular nuevo sin nada de tecnología
samsung.set_pantalla("IPC")
samsung.set_almacenamiento(256)
samsung.set_camara(64)
samsung.set_forma("CURVA")
samsung.set_ram(8)
print(samsung.__str__())
# samsung.encender()

print('Comprobando sus componentes') if samsung.get_encendido(
) else print('Aún no se puede encender el Celular')

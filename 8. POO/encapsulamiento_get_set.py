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


samsung = Celular()  # Celular nuevo sin nada de tecnología
samsung.set_pantalla("IPC")
samsung.set_almacenamiento(256)
samsung.set_camara(64)
samsung.set_forma("CURVA")
samsung.set_ram(8)

xiaomi = Celular()  # La misma base de donde partió samsung
xiaomi.set_pantalla("AMOLED")
xiaomi.set_almacenamiento(128)
xiaomi.set_camara(48)
xiaomi.set_forma("RECTANGULAR")
xiaomi.set_ram(4)

print(f'Celular Samsung \n')
print(f'''Pantalla -> {samsung.get_pantalla()} 
    Almacenamiento -> {samsung.get_almacenamient()} GB
    Forma -> {samsung.get_forma()}
    Ram -> {samsung.get_ram()} GB
    Cámara -> {samsung.get_camara()} MegaPixeles
''')

print(f'\nCelular Xiaomi \n')
print(f'''Pantalla -> {xiaomi.get_pantalla()} 
    Almacenamiento -> {xiaomi.get_almacenamient()} GB
    Forma -> {xiaomi.get_forma()}
    Ram -> {xiaomi.get_ram()} GB
    Cámara -> {xiaomi.get_camara()} MegaPixeles
''')


class Celular: #  Molde principal
    # Atributos
    pantalla = ""
    forma = ""
    ram = 0
    almacenamiento = 0
    camara = 0

    def __init__(self, pantall, forma, ram, almacenamiento, camara):
        self.pantalla = pantall
        self.forma = forma
        self.ram = ram
        self.almacenamiento = almacenamiento
        self.camara = camara

samsung = Celular("AMOLED", "RECTANGULO", 6, 128, 48)
print(type(samsung))
print(samsung.almacenamiento)
print(samsung.camara)
print(samsung.forma)
print(samsung.pantalla)

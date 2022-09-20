import math


class Persona:
    def __init__(self, nombre, apellido, altura, peso):
        self.nombre = nombre
        self.apellido = apellido
        self.altura = altura
        self.peso = peso

    def calcular_imc(self):
        return self.peso / math.pow(self.altura, 2)


class Trabajador(Persona):
    def __init__(self, nombre, apellido, altura, peso):
        Persona.nombre = nombre
        Persona.apellido = apellido
        Persona.altura = altura
        Persona.peso = peso

    def trabajar():
        return "Estoy trabajando"


class Instituto:
    def __init__(self, nombre):
        self.nombre_ins = nombre

    def estudiando(self):
        return f"estoy estudiendo en: "+self.nombre_ins


class Estudiante(Trabajador, Instituto):
    def __init__(self, nombre, apellido, altura, peso, nombre_ins):
        Trabajador.nombre = nombre
        Trabajador.apellido = apellido
        Trabajador.altura = altura
        Trabajador.peso = peso
        Instituto.nombre_ins = nombre_ins

    def estudiar(self):
        return " me gusta estudiar"


estudiante = Estudiante("Juan", "Estevez", 1.80, 70, "Universidad xxx")
print(estudiante.calcular_imc())
print(estudiante.estudiando())
print(estudiante.estudiar())

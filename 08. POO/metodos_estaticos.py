class Persona:

    variable_clase = "Esta es una variable de clase"

    def __init__(self, variable_instancia):
        self._variable_de_instancia = variable_instancia

    def get_variable_instancia(self):
        self._variable_de_instancia

    def metodo_normal(self):
        return "este es un método normal"

    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)

    @staticmethod
    def metodo_estatico():
        print(Persona.variable_clase)

Persona.metodo_clase()
Persona.metodo_estatico()

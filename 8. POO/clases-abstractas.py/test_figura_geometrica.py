from Cuadrado import Cuadrado
from Triangulo import Triangulo

print("Creando un objeto de tipo CUADRADO".center(50, "-"))
cuadrado = Cuadrado(ancho=5, alto=5)
cuadrado.set_alto(7)
cuadrado.set_ancho(7)
print(f"Calculando el área del cuadrado {cuadrado.calcular_area()}")
print(cuadrado)

print("----------------------------------")
print("Creando un objeto de tipo TRIÁNGULO".center(50, "-"))
triangulo = Triangulo(ancho=5, alto=5)
triangulo.set_alto(4)
triangulo.set_ancho(6)
print(f"Calculando el área del triángulo {triangulo.calcular_area()}")
print(triangulo)

from Cuadrado import Cuadrado

print("Creando un objeto de tipo CUADRADO".center(50, "-"))
cuadrado = Cuadrado(ancho=5, alto=5)
cuadrado.set_alto(7)
cuadrado.set_ancho(7)
print(f"Calculando el área del cuadrado {cuadrado.calcular_area()}")
print(cuadrado)

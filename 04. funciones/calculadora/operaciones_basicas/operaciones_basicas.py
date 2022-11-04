import math


sumar = lambda a, b: (a + b)
restar = lambda a, b: a-b
multiplicar = lambda a, b: a*b
potencia = lambda a, b: pow(a, b)
raizCubica = lambda a: pow(a, (1/3))

def dividir(a, b):
    if b == 0:
        return 'No es posible dividir por 0, Intenta nuevamente'
    else:
        return a / b


def modulo(num1, num2):
    if num2 != 0:
        return num1 % num2
    else:
        return "No es posible dividir por 0"


def raiz(num):
    if num >= 0:
        return math.sqrt(num)
    else:
        num * -1
        return math.sqrt(num), "i"




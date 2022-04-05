from operaciones_basicas.operaciones_basicas import *

def operaciones_basicas():
    a = int(input("\nIngrese un número  "))
    b = int(input("Ingrese otro número  "))
    return f'''    
    Suma:             {a} + {b} = {sumar(a, b)}
    Resta:            {a} - {b} = {restar(a, b)}
    Multiplicación:   {a} x {b} = {multiplicar(a, b)}
    División:         {a} / {b} = {dividir(a, b)}
    Módulo:           {a} % {b} = {modulo(a, b)}
    Raiz Cuadrada {a}:   {raiz(a)}
    Raiz cuadrada {b}:   {raiz(b)}
    Potencia:         {a} ^ {b} = {potencia(a, b)}
    Raiz Cúbica {a}:    {raizCubica(a)}
    Raiz Cúbica {b}:    {raizCubica(b)}
        '''
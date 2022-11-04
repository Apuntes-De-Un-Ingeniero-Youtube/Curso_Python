"""
    En 1937 un matemático alemán llamado Lothar Collartz formuló una hipótesis intrigante 
    (aún no se ha comprobado) que se puede describir de la siguinte manera:

        1. Toma cualquier número entero que no sea negativo y que no sea 0 y asignale el nombre c0
        2. Si es par, evalúa un nuevo c0 como c0 % 2
        3. De lo contrario, si es impar, evalúe un nuevo c0 como 3 x c0 + 1
        4. Si c0 es diferente de 1, salta al punto 2

    La hipótesis dice que, independientemente del valor inicial de c0, el valor siempre tiende a 1.

    Por supuesto, es una tarea extremadamente compleja usar una computadora para probar la hipótesis de 
    cualquier número natural (incluso puede requerir inteligencia artificial), pero puede usar python 
    para verificar algunos números individuales. Tal vez incluso el que refutaría la hipotesis 

    Escriba un programa que lea un número natural y ejecute los pasos anteriores siempre que c0 sea
    diferente de 1. También queremos que cuente los pasos necesarios para lograr el objetivo. Tu código
    también debe mostrar los pasos intermedios de c0.
"""


def collartz():
    c0 = int(input('Ingrese un número mayor a 0  '))
    pasos = 1

    if c0 > 0:
        while c0 != 1:
            if c0 % 2 == 0:
                c0 / 2
            else:
                c0 = 3 * c0 + 1

            print(f'Paso {pasos}: c0 = {c0}')
            pasos += 1
    else:
        print('Debe ingresar un número mayor a 0 ')

    print(f'\nResultado final de c0 = {c0}: Pasos totales {pasos}')

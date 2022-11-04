import time


def decorador(func):
    def div_text(*args, **kwargs):
        tiempo = time.time() # Devuelve la hora actual
        print('Efectuando la división')
        resultado = func(*args, **kwargs) 
        tiempo2 = time.time()
        print('La función tardó {0} segundos en ejecutarse '.format(tiempo2 - tiempo))
        return resultado
    return div_text


@decorador
def division(num1, num2, num3=3):
    return num1 / num2 / num3


print(division(5, 2))

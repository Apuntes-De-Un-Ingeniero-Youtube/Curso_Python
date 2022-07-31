# Localiza el error en el siguiente bloque de código. Crea una excepción para evitar
# que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:

try:
    colores = {'rojo': 'red', 'verde': 'green', 'negro': 'black'}
    colores['blanco']
except KeyError as ke:
    print('Se ha cometido un error de tipo KeyError, el cual sucede al tratar de acceder a una llave que no existe en un diccionario')
    print('Una posible solución puede ser crear ese llave con su respectivo valor o simplemente acceder a una llave válida')

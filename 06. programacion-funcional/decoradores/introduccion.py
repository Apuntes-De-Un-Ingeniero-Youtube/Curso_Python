# def mi_decorador(funcion):  # suma
#     def nueva_funcion(a, b):  # 1, 2
#         print("Se va a llamar")
#         c = funcion(a, b)  # suma(1, 2)
#         print("Se ha llamado")
#         return c  # 3
#     return nueva_funcion


# @mi_decorador
# def suma(a, b):
#     print("Entra en funcion suma")
#     return a + b


# @mi_decorador
# def resta(a, b):
#     print("Entra en funcion resta")
#     return a - b


# print(suma(1, 2))
# print(resta(5, 3))

def mi_decorador(arg):
    def decorador_real(funcion):
        def nueva_funcion(a, b):
            print(arg)
            c = funcion(a, b)
            print(arg)
            return c
        return nueva_funcion
    return decorador_real


@mi_decorador("Imprimer esto antes y después")
def suma(a, b):
    print("Entra en funcion suma")
    return a + b


print(suma(7, 4))

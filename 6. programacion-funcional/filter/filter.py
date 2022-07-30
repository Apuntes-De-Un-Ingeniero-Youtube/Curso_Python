# ------------------ Introducción ---------------------------
# filter(funcion o fitro, iterable a filtrar)
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# def func(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False


resultado = filter(lambda x: x % 2 == 0, numeros)
print(list(resultado))
# -----------------------------------------------------------

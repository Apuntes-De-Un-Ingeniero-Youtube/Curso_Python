# La función itera a través de todos los elementos en el iterable dado y ejecuta el function 
# pasamos como argumento en cada uno de ellos.

# map(funcion, iterable)

# sin utilizar lambdas
def empezar_con_A(x):
    return x[0] == "M"

frutas = ["Banana", "Manzana", "Maracuyá", "Mango", "Anón"]
objeto_map = map(empezar_con_A, frutas)
print(list(objeto_map))

# utilizando lambdas
frutas = ["Banana", "Manzana", "Maracuyá", "Mango", "Anón"]
objeto_map = map(lambda x: x[0] == "B", frutas)
print(list(objeto_map))
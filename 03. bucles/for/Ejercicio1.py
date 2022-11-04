"""
    Realizar un programa que pida al usuario la cantidad de asiatentes a una reunion, 
    pida la edad de cada asistente utilizando un for e imprima al final del programa
    el asistente con mayor y menor edad de todos
"""
asistentes = int(input("Ingrese la cantidad de asistentes por favor  ")) #4
mayor = -1 # 90
menor = 99999 # 5

for i in range(asistentes): # 1
    edad = int(input(f"Ingrese la edad del asistente N° {i+1} "))
    if edad > mayor:
        mayor = edad
    elif edad < menor:
        menor = edad

print("\nEl asistente con mayor edad tiene : ", mayor, " años"
      "\nEl asistente con menor edad tiene : ", menor, " años")
"""
    Un mago junior ha elegido un número secreto. Lo ha escondido en una variable llamada
    numeroSecreto. Quiere que todos los que ejecutan su programa jueguen al juego
    "Adivina el número secreto" y adivina que número ha elegido para ellos.¡Quienes no
    adivinen el número quedarán atrapados en un ciclo sin fin para siempre! Desafortunadamente,
    él no sabe cómo completar el código

    Tu tarea es ayudar al mago a completar su código en el editor de texto del tal manera que
    el código:

        * Pedirá al usuario que ingrese un número entero.
        * Utiliza un cilo while
        * Comprobará si el número ingresado por el usuario es el mismo que el número escogido por
          el mago. Si el número elegido por el usuario es diferente del número secreto del mago 
          el usuario deberá ver el mensaje "¡Ja, ja! ¡Estás atrapado en mi ciclo¡" y se le 
          solicitará que ingrese un número nuevamente. Si el número ingresado por el usuario
          coincide con el número escogido por el mago, el número debe imprimirse en la pantalla, y
          el mago debe decir las siguientes palabras "¡Bien hecho, muggle! Eres libre ahora"
    
    ¡El mago cuenta contigo! No lo decepciones.
"""
import random

numeroSecreto = random.randint(0, 10)
numero = int(input('Ingrese un número entre 0 y 10 por favor  ')) # 5
intentos = 0

if 0 <= numero <= 10:
    while numero != numeroSecreto:
        print("¡Ja, ja! ¡Estás atrapado en mi ciclo¡")
        intentos += 1
        numero = int(input('Ingrese un número entre 0 y 10 por favor  ')) # 4
    print(f"¡Bien hecho, muggle! Eres libre ahora  ->  Intentos {intentos}")
else:
    print('El número debe estar entre 0 y 10, Intenta nuevamente.')

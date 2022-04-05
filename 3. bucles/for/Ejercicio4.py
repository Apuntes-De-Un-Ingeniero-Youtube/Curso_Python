"""
    Un grupo de amigos decide organizar un juego de estrategia, para lo cual forman dos 
    equipos de 6 integrantes cada uno, donde un integrante de cada equipo es el “jefe” y 
    los otros 5 son sus “oficiales”. La regla más importante del juego es que sólo se 
    comunicarán mediante un canal común, por lo que deben buscar la forma de ocultar el 
    contenido de sus mensajes. 
    
    
    Uno de los equipos decide utilizar un método antiguo de 
    encriptación llamado “la cifra del césar”, que consiste en correr cada letra del 
    mensaje –considerando la posición de cada una en el alfabeto– una determinada cantidad 
    de lugares. Ejemplo: si el corrimiento es de 2 lugares, la palabra “ATAQUE” se 
    transforma en “CVCSWG”.
    Cada día, el “jefe” del equipo debe enviar un mensaje a cada uno de sus oficiales. 
    Escribir un programa que permita encriptar los 5 mensajes. El corrimiento 
    (cantidad de lugares que se correrán las letras) será dado por el usuario antes de 
    comenzar a encriptar. Los 5 mensajes usarán el mismo corrimiento.
    Nota: si el alfabeto termina antes de poder correr la cantidad de lugares necesarios, 
    se vuelve a comenzar desde la letra “a”. Ejemplo: la palabra “EXTRA” corrida 3 lugares 
    se convierte en “HAWUD”. Utilizando el alfabeto español, de 27 letras, el siguiente 
    cálculo matemático permite volver a comenzar por el principio una vez que se llegó a 
    la “z”: (índice de la letra a correr+corrimiento)%27
    Sólo se encriptarán las letras de los mensajes, dejando al resto de caracteres sin 
    modificación
"""
alfabeto = 'abcdefghijklmnñopqrstuvwxyz' # 27 letras del alfabeto
corrimiento = int(input('Ingrese el corriemiento  ')) # 3

for i in range(5): # 5
    mensaje = input('Ingrese el mensaje a encriptar  ') 
    encriptado = ''
    for caracter in mensaje: # H o l a
        if caracter.lower() in alfabeto: # h
            indice = alfabeto.find(caracter.lower()) # 7
            indice = (indice + corrimiento) % 27 
            encriptado = encriptado + alfabeto[indice]
        else:
            encriptado = encriptado + caracter

    print(encriptado)
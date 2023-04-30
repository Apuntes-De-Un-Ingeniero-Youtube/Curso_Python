import tkinter as tk

# Creamos la ventana principal de la aplicación
ventana = tk.Tk()

# ------ Etiqueta LABEL ------
# Creamos un widget de etiqueta y lo ubicamos en la ventana
etiqueta = tk.Label(ventana, text="¡Hola, mundo!")
etiqueta.pack()
# --------------------------------------------

# ------ Input o entrada de texto ENTRY ------
# Creamos un widget de entrada y lo ubicamos en la ventana
entrada = tk.Entry(ventana)
entrada.pack()


# Creamos una función que se ejecutará cuando se presione el botón
def mostrar_texto():
    texto = entrada.get()
    print(texto)

# Creamos un botón que ejecutará la función cuando se presione
boton = tk.Button(ventana, text="Mostrar texto", command=mostrar_texto)
boton.pack()
# --------------------------------------------


# ------ Textarea TEXT ------
# Creamos un widget de texto y lo ubicamos en la ventana
texto = tk.Text(ventana)
texto.pack()

# Creamos una función que se ejecutará cuando se presione el botón
def mostrar_texto():
    contenido = texto.get("1.0", tk.END)
    print(contenido)

# Creamos un botón que ejecutará la función cuando se presione
boton2 = tk.Button(ventana, text="Mostrar texto", command=mostrar_texto)
boton2.pack()
# --------------------------------------------

# Ejecutamos el bucle principal de eventos para mantener la ventana abierta
ventana.mainloop()

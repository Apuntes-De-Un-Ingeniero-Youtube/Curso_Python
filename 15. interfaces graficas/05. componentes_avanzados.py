import tkinter as tk

# Creamos la ventana principal de la aplicación
ventana = tk.Tk()

# ------ Componente de dibujo CANVAS ------
# Creamos un widget Canvas y lo ubicamos en la ventana
canvas = tk.Canvas(ventana, width=200, height=200, bg='white')
canvas.pack()

# Dibujamos una línea en el canvas
canvas.create_line(0, 0, 200, 200)

# Dibujamos un rectángulo en el canvas
canvas.create_rectangle(50, 50, 150, 150, fill='red')

# Dibujamos un óvalo en el canvas
canvas.create_oval(50, 50, 150, 150, fill='green')
# -----------------------------------------------

# ------ Componente MENÚ ------
# Creamos una función para manejar la acción del menú


def accion_menu():
    print("Se seleccionó una opción de menú")


# Creamos un objeto menú
menu = tk.Menu(ventana)

# Agregamos opciones al menú
menu_opcion1 = tk.Menu(menu)
menu_opcion1.add_command(label='Opción 1', command=accion_menu)
menu_opcion1.add_command(label='Opción 2', command=accion_menu)
menu_opcion1.add_command(label='Opción 3', command=accion_menu)
menu.add_cascade(label='Opciones', menu=menu_opcion1)

# Agregamos el menú a la ventana principal
ventana.config(menu=menu)
# -----------------------------------------------

# ------ Componente select LISTBOX ------
# Creamos un widget Listbox y lo ubicamos en la ventana
listbox = tk.Listbox(ventana)
listbox.pack()

# Agregamos algunos elementos al Listbox
listbox.insert(0, "Elemento 1")
listbox.insert(1, "Elemento 2")
listbox.insert(2, "Elemento 3")

# Creamos una función para manejar la selección de un elemento del Listbox


def seleccion_elemento(event):
    seleccion = listbox.curselection()
    if seleccion:
        index = seleccion[0]
        valor = listbox.get(index)
        print("Se seleccionó el elemento:", valor)


# Asociamos la función con el evento de selección de un elemento del Listbox
listbox.bind("<<ListboxSelect>>", seleccion_elemento)
# -----------------------------------------------

# Ejecutamos el bucle principal de eventos para mantener la ventana abierta
ventana.mainloop()

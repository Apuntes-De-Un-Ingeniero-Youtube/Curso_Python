from tkinter import *
from tkinter import messagebox
import sqlite3

# Creamos la conexión a la base de datos
conn = sqlite3.connect('15. interfaces graficas/usuarios.db')

# Creamos la tabla de usuarios
conn.execute('''CREATE TABLE IF NOT EXISTS usuarios
             (ID INTEGER PRIMARY KEY AUTOINCREMENT,
             NOMBRE TEXT NOT NULL,
             EDAD INT NOT NULL);''')

# Función para agregar un usuario a la base de datos


def agregar_usuario():
    nombre = nombre_entry.get()
    edad = edad_entry.get()
    conn.execute(
        f"INSERT INTO usuarios (NOMBRE, EDAD) VALUES ('{nombre}', {edad})")
    conn.commit()
    messagebox.showinfo("Éxito", "Usuario agregado correctamente")

# Función para mostrar los usuarios de la base de datos


def mostrar_usuarios():
    usuarios = conn.execute("SELECT * FROM usuarios").fetchall()
    usuarios_text.delete(1.0, END)
    for usuario in usuarios:
        usuarios_text.insert(
            END, f"ID: {usuario[0]}\nNombre: {usuario[1]}\nEdad: {usuario[2]}\n\n")

# Función para actualizar un usuario en la base de datos


def actualizar_usuario():
    id = id_entry.get()
    nombre = nombre_entry.get()
    edad = edad_entry.get()
    conn.execute(
        f"UPDATE usuarios SET NOMBRE = '{nombre}', EDAD = {edad} WHERE ID = {id}")
    conn.commit()
    messagebox.showinfo("Éxito", "Usuario actualizado correctamente")

# Función para eliminar un usuario de la base de datos


def eliminar_usuario():
    id = id_entry.get()
    conn.execute(f"DELETE FROM usuarios WHERE ID = {id}")
    conn.commit()
    messagebox.showinfo("Éxito", "Usuario eliminado correctamente")


# Creamos la ventana principal
root = Tk()
root.title("CRUD de Usuarios")

# Creamos los componentes de la interfaz de usuario
Label(root, text="ID").grid(row=0, column=0)
Label(root, text="Nombre").grid(row=1, column=0)
Label(root, text="Edad").grid(row=2, column=0)

id_entry = Entry(root)
nombre_entry = Entry(root)
edad_entry = Entry(root)

id_entry.grid(row=0, column=1)
nombre_entry.grid(row=1, column=1)
edad_entry.grid(row=2, column=1)

agregar_button = Button(root, text="Agregar", command=agregar_usuario)
mostrar_button = Button(root, text="Mostrar", command=mostrar_usuarios)
actualizar_button = Button(root, text="Actualizar", command=actualizar_usuario)
eliminar_button = Button(root, text="Eliminar", command=eliminar_usuario)

agregar_button.grid(row=3, column=0)
mostrar_button.grid(row=3, column=1)
actualizar_button.grid(row=3, column=2)
eliminar_button.grid(row=3, column=3)

usuarios_text = Text(root, height=10, width=50)
usuarios_text.grid(row=4, columnspan=4)

root.mainloop()

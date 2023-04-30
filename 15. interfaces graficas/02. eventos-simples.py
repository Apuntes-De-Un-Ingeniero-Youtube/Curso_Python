import tkinter as tk
from tkinter import ttk

# Creación ventana
ventana = tk.Tk()

# Asiganción tamaño a la ventana
ventana.geometry("600x400")

# Cambiando titulo
ventana.title("Banco xyz")


def evento_boton_enviar():
    enviar.config(text="Mensaje enviado")
    mensaje_enviado = ttk.Button(ventana, text="Credenciales correctas")
    mensaje_enviado.pack()


# Botón
enviar = ttk.Button(ventana, text="Enviar", command=evento_boton_enviar)
enviar.pack()

# Inicialización ventana
ventana.mainloop()

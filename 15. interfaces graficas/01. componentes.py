import tkinter as tk
from tkinter import ttk

# Creación ventana
ventana = tk.Tk()

# Asiganción tamaño a la ventana
ventana.geometry("600x400")

# Cambiando titulo
ventana.title("Banco xyz")

# Botón
enviar = ttk.Button(ventana, text="Enviar")
enviar.pack()

# Inicialización ventana
ventana.mainloop()

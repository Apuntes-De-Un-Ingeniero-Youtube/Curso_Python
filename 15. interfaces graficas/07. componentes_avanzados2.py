import tkinter as tk

ventana = tk.Tk()


scale = tk.Scale(ventana, from_=25, to=50, orient="horizontal")
scale.pack(pady=10)


def imprimir_scale(valor):
    print(f"Seleccionó el valor: {valor}")


scale.config(command=imprimir_scale)

var_checkbox = tk.BooleanVar()
checkbox = tk.Checkbutton(ventana, text="Habilitar", variable=var_checkbox)
checkbox.pack()


def click_checkbox():
    print("Hola") if var_checkbox.get() else print("chao")


checkbox.config(command=click_checkbox)

var_radio = tk.StringVar()
radiobutton = tk.Radiobutton(
    ventana, text="Opción 1", variable=var_radio, value="Opcion primera")
radiobutton.pack()
radiobutton1 = tk.Radiobutton(
    ventana, text="Opción 2", variable=var_radio, value="Opcion segunda")
radiobutton1.pack()
radiobutton2 = tk.Radiobutton(
    ventana, text="Opción 3", variable=var_radio, value="Opcion tercera")
radiobutton2.pack()
radiobutton3 = tk.Radiobutton(
    ventana, text="Opción 4", variable=var_radio, value="Opcion cuarta")
radiobutton3.pack()


def seleccion_radio():
    print("Seleccionó "+ var_radio.get())

radiobutton.config(command=seleccion_radio)
radiobutton1.config(command=seleccion_radio)
radiobutton2.config(command=seleccion_radio)
radiobutton3.config(command=seleccion_radio)

ventana.mainloop()

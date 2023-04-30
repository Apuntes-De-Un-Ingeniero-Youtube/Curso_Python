import tkinter as tk

ventana = tk.Tk()

scrollbar = tk.Scrollbar(ventana)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

lista = tk.Listbox(ventana, yscrollcommand=scrollbar.set)
lista.pack(side=tk.LEFT)

for i in range(100):
    lista.insert(tk.END, "Elemento "+str(i))

scrollbar.config(command=lista.yview)
lista.config(yscrollcommand=scrollbar.set)

ventana.mainloop()

import tkinter as tk # Importando librería
from tkinter import * # Importando conponentes de tkinter
from tkinter import ttk # Importando tema ttk


class karl(Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.pack()
        self.master.title("Karlos")
        self.button1 = Button(self, text="CLICK HERE", width=25,
                              command=self.new_window)
        self.button1.grid(row=0, column=1, columnspan=2, sticky=W+E+N+S)

    def new_window(self):
        self.newWindow = karl2()


class karl2(Frame):
    def __init__(self):
        new = tk.Frame.__init__(self)
        new = Toplevel(self)
        new.title("karlos More Window")
        new.button = tk.Button(text="PRESS TO CLOSE", width=25,
                               command=self.close_window)
        new.button.pack()

    def close_window(self):
        self.destroy()


def main():
    karl().mainloop()


if __name__ == '__main__':
    main()

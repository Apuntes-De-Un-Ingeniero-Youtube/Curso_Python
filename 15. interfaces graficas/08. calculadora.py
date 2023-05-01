import tkinter as tk


class Calculator(object):
    '''Esta clase construye y manipula una calculadora gráfica'''

    def __init__(self, parent=tk.Tk()):
        self.parent = parent
        self.parent.title("PyCalc - Calculator")
        self.parent.option_add("*Font", "Verdana 12 normal")
        self.parent.iconbitmap("15. interfaces graficas/icons/calculadora.ico")

        # Variable de control, utilizada en método key_press
        self.decimal_point_open = False

        # Variable que contiene la expresión de punto para calculo
        self.math_expression = None

        # Menú
        menu_bar = tk.Menu(self.parent)
        menu_bar.add_command(label="About", command=self.about)
        self.parent.config(menu=menu_bar)

        # Elementos del display
        self.display_stringvar = tk.StringVar()
        display_entry_validate = (self.parent.register(
            self.only_number_entry), '%S', '%d')
        self.display = tk.Entry(self.parent, font=("Verdana", 20, "normal"), validate="key",
                                validatecommand=display_entry_validate, textvariable=self.display_stringvar)
        self.display.bind('<Return>', self.calc_expression)

        # Elementos del teclado numérico
        self.btn0 = tk.Button(self.parent, text="0",
                              command=lambda: self.button_press('0'))
        self.btn1 = tk.Button(self.parent, text="1",
                              command=lambda: self.button_press('1'))
        self.btn2 = tk.Button(self.parent, text="2",
                              command=lambda: self.button_press('2'))
        self.btn3 = tk.Button(self.parent, text="3",
                              command=lambda: self.button_press('3'))
        self.btn4 = tk.Button(self.parent, text="4",
                              command=lambda: self.button_press('4'))
        self.btn5 = tk.Button(self.parent, text="5",
                              command=lambda: self.button_press('5'))
        self.btn6 = tk.Button(self.parent, text="6",
                              command=lambda: self.button_press('6'))
        self.btn7 = tk.Button(self.parent, text="7",
                              command=lambda: self.button_press('7'))
        self.btn8 = tk.Button(self.parent, text="8",
                              command=lambda: self.button_press('8'))
        self.btn9 = tk.Button(self.parent, text="9",
                              command=lambda: self.button_press('9'))
        self.btn_plus = tk.Button(
            self.parent, text="+", command=lambda: self.button_press('+'))
        self.btn_menos = tk.Button(
            self.parent, text="-", command=lambda: self.button_press('-'))
        self.btn_multiplica = tk.Button(
            self.parent, text="*", command=lambda: self.button_press('*'))
        self.btn_divide = tk.Button(
            self.parent, text="/", command=lambda: self.button_press('/'))
        self.btn_point = tk.Button(
            self.parent, text=".", command=lambda: self.button_press('.'))
        self.btn_igual = tk.Button(
            self.parent, text="=", command=lambda: self.button_press('='))
        self.btn_clean = tk.Button(
            self.parent, text="Clean", command=self.clean)
        self.btn_close = tk.Button(
            self.parent, text="Close(Esc)", command=lambda: self.parent.destroy())
        self.parent.bind("<Escape>", lambda event=None: self.parent.destroy())
        self.mount_gui()
        self.parent.mainloop()

    # Monta y configura los componentes gráficos
    def mount_gui(self):
        self.display.grid(row=0, column=0, columnspan=4,
                          sticky="ewns", ipady=5, padx=2, pady=2)
        self.btn0.grid(row=4, column=0, sticky="ewns", padx=2, pady=2)
        self.btn1.grid(row=3, column=0, sticky="ewns", padx=2, pady=2)
        self.btn2.grid(row=3, column=1, sticky="ewns", padx=2, pady=2)
        self.btn3.grid(row=3, column=2, sticky="ewns", padx=2, pady=2)
        self.btn4.grid(row=2, column=0, sticky="ewns", padx=2, pady=2)
        self.btn5.grid(row=2, column=1, sticky="ewns", padx=2, pady=2)
        self.btn6.grid(row=2, column=2, sticky="ewns", padx=2, pady=2)
        self.btn7.grid(row=1, column=0, sticky="ewns", padx=2, pady=2)
        self.btn8.grid(row=1, column=1, sticky="ewns", padx=2, pady=2)
        self.btn9.grid(row=1, column=2, sticky="ewns", padx=2, pady=2)
        self.btn_plus.grid(row=3, column=3, sticky="ewns", padx=2, pady=2)
        self.btn_menos.grid(row=2, column=3, sticky="ewns", padx=2, pady=2)
        self.btn_divide.grid(row=4, column=3, sticky="ewns", padx=2, pady=2)
        self.btn_multiplica.grid(
            row=1, column=3, sticky="ewns", padx=2, pady=2)
        self.btn_point.grid(row=4, column=1, sticky="ewns", padx=2, pady=2)
        self.btn_igual.grid(row=4, column=2, sticky="ewns", padx=2, pady=2)
        self.btn_clean.grid(row=5, column=0, columnspan=2,
                            sticky="ewns", padx=2, pady=2)
        self.btn_close.grid(row=5, column=2, columnspan=2,
                            sticky="ewns", padx=2, pady=2)

    # Limpia el display
    def clean(self):
        self.display_stringvar.set("")
        self.decimal_point_open = False

    # Tecla About
    def about(self):
        about_window = tk.Toplevel(self.parent)
        about_window.title("PyCalc - About")
        about_window.iconbitmap("calculadora.ico")
        tk.Label(about_window, text="PyCalc", font=("Verdana", 15, "bold")).grid(
            row=0, column=0, padx=5, pady=5, sticky="s")
        tk.Label(about_window, text="Simple Calculator").grid(
            row=1, column=0, padx=5, pady=5, sticky="s")
        tk.Label(about_window, text="Made with Python 3 and Tkinter").grid(
            row=2, column=0, sticky="s", padx=5)
        tk.Label(about_window, text="Development by Juan Carlos Estevez Vargas").grid(row=3,
                                                                                      column=0, sticky="s", padx=5)

    # Validador de Entrys solamente expresiones matemáticas válidas
    def only_number_entry(self, key_press, cod):
        expression_now = self.display_stringvar.get()
        num_chars_now = len(expression_now)

        if(num_chars_now == 0):
            valid_chars_for_init = "0123456789"
            return key_press in valid_chars_for_init
        else:
            last_char = expression_now[num_chars_now-1]

            # Si el último elemento insertado es un operador, solo acepta números o retroceso
            if(last_char in "+-*/" and key_press in "+-*/." and cod == '1'):
                return False

            # Controla el uso del punto decimal
            # Evita dos operadores seguidos
            elif(last_char in "+-*/" and key_press in "+-*/." and cod == '0'):
                return True
            elif(last_char == '.' and key_press in "+-*/." and cod == '1'):
                return False
            elif(last_char == '.' and key_press in "+-*/." and cod == '0'):
                return True
            elif(self.decimal_point_open and key_press == '.'):
                return False
            elif(not self.decimal_point_open and key_press == '.'):
                self.decimal_point_open = True
                return True
            elif(last_char in "0123456789" and key_press in "+-*/"):
                self.decimal_point_open = False
                return True

    # Botón de interfaz presionado
    def button_press(self, bt):
        expresion_now = self.display_stringvar.get()
        char_num = len(expresion_now)

        # Define caracteres válidos para el comienzo de la expresión
        if(char_num == 0):
            valid_chars_for_init = "0123456789"
            if(bt in valid_chars_for_init):
                expresion_now += bt
                self.display_stringvar.set(expresion_now)
        else:
            # Controla do uso de punto decimal
            last_char = expresion_now[char_num - 1]
            if(bt == '.' and not last_char in "+-*/"):
                if(self.decimal_point_open):
                    print("punto decimal no disponible")
                else:
                    expresion_now += bt
                    self.display_stringvar.set(expresion_now)
                    self.decimal_point_open = True
            else:
                if(last_char in ".0123456789" and bt in "0123456789"):
                    expresion_now += bt
                    self.display_stringvar.set(expresion_now)
                elif(last_char in "0123456789" and not self.decimal_point_open and bt in "+-*/"):
                    expresion_now += bt
                    self.display_stringvar.set(expresion_now)
                elif(self.decimal_point_open and not last_char == '.' and bt in "+-*/"):
                    expresion_now += bt
                    self.display_stringvar.set(expresion_now)
                    self.decimal_point_open = False
                # Controlar el uso de operadores
                elif(last_char in "+-*/" and bt in "0123456789"):
                    expresion_now += bt
                    self.display_stringvar.set(expresion_now)
                # Botón = presionado, obtener resultado
                elif(bt == '=' and last_char in "0123456789"):
                    # Calcula la expresión
                    self.calc_expression()

    def prepare_expression(self):
        elementos = []
        indice = 0
        for char in self.display_stringvar.get():
            # Inicializar la lista con el primer número
            if(len(elementos) == 0 and char in "0123456789"):
                elementos.append(char)
            # Nuevo operador como nuevo elemento de lista
            elif(len(elementos) > 0 and char in "+-*/"):
                elementos.append(char)
                indice += 1
            elif(elementos[indice] in "+-*/"):
                elementos.append(char)
                indice += 1
            else:
                elementos[indice] += char
        # Guarda la expresión preparada como un atributo del objeto
        self.math_expression = elementos

     # Calcula la expresión
    def calc_expression(self, event=None):
        self.prepare_expression()
        # multiplicación y división, precedencia: lo que ocurra primero de izquierda a derecha
        while ("*" in self.math_expression or "/" in self.math_expression):
            indice = 0
            for element in self.math_expression:
                if (element == '*'):
                    v1 = float(self.math_expression[indice - 1])
                    v2 = float(self.math_expression[indice + 1])
                    result = str(v1 * v2)
                    self.math_expression[indice] = result
                    self.math_expression.pop(indice + 1)
                    self.math_expression.pop(indice - 1)
                    indice += 1
                    break
                elif (element == '/'):
                    v1 = float(self.math_expression[indice - 1])
                    v2 = float(self.math_expression[indice + 1])
                    result = str(v1 / v2)
                    self.math_expression[indice] = result
                    self.math_expression.pop(indice + 1)
                    self.math_expression.pop(indice - 1)
                    indice += 1
                    break
                else:
                    indice += 1

        # Adición y sustracción
        # Repetir hasta que solo quede el resultado
        while (len(self.math_expression) > 1):
            indice = 0
            for element in self.math_expression:
                if (element == '+'):
                    v1 = float(self.math_expression[indice - 1])
                    v2 = float(self.math_expression[indice + 1])
                    result = str(v1 + v2)
                    self.math_expression[indice] = result
                    self.math_expression.pop(indice + 1)
                    self.math_expression.pop(indice - 1)
                    indice += 1
                    break
                if (element == '-'):
                    v1 = float(self.math_expression[indice - 1])
                    v2 = float(self.math_expression[indice + 1])
                    result = str(v1 - v2)
                    self.math_expression[indice] = result
                    self.math_expression.pop(indice + 1)
                    self.math_expression.pop(indice - 1)
                    indice += 1
                    break
                else:
                    indice += 1
        final_result = str(round(float(self.math_expression[0]), 1))
        # Insertar el resultado en la pantalla
        self.display_stringvar.set(final_result)


if __name__ == "__main__":
    calculadora = Calculator()

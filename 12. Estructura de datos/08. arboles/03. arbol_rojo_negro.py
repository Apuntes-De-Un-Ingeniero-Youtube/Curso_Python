# Nodo de árbol rojo-negro
class RBN(object):
    def __init__(self, data):
        self.data = data  # Campo de datos
        self.color = 0  # 0 rojo 1 negro
        self.left = None
        self.right = None
        self.parent = None


# Árbol negro rojo
class RBT(object):
    def __init__(self):
        self.root = None

    # Recorrido de orden medio
    def midTraverse(self, x):
        if x == None:
            return
        self.midTraverse(x.left)
        colorStr = 'negro' if x.color == 1 else 'rojo'
        parentStr = 'Padre =' + ('No tiene' if x.parent ==
                                 None else str(x.parent.data))
        print(x.data, colorStr, parentStr)
        self.midTraverse(x.right)

    # Agregar un nodo
    def add(self, x):
        # Si no hay un nodo raíz como nodo raíz
        if self.root == None:
            self.root = x
            x.color = 1  # El nodo raíz es negro
            # print ('Agregado exitosamente', x.data)
            return

        # Encuentre una posición de inserción adecuada
        p = self.root
        while p != None:
            if x.data < p.data:
                if p.left == None:
                    p.left = x
                    x.parent = p
                    # print ('Agregado exitosamente', x.data)
                    self.addFix(x)
                    break
                p = p.left
            else:
                if p.right == None:
                    p.right = x
                    x.parent = p
                    # print ('Agregado exitosamente', x.data)
                    self.addFix(x)
                    break
                p = p.right

    # Ajusta el árbol rojo-negro
    def addFix(self, x):
        while True:
            if x == self.root:  # Si se procesa el nodo raíz, el color es negro
                x.color = 1
                return
            p = x.parent  # Papi
            if p.color == 1 or x.color == 1:  # Mientras uno de mí y papá sea negro, no puede ser doblemente rojo, luego regrese
                return
            # A continuación, analiza la situación de Red Dad
            g = p.parent  # El abuelo Red Dad debe tener un padre, porque el rojo nunca es el nodo raíz
            # El tío El tío puede ser un nodo vacío
            u = g.left if p == g.right else g.right
            if u != None and u.color == 0:  # Luego coloréalo y continúa ajustando del abuelo
                u.color = p.color = 1  # Tío y papá se ponen negros
                g.color = 0  # El abuelo se pone rojo
                x = g  # x apunta al abuelo y luego continúa el ciclo
                continue
            # A continuación, analiza la situación del tío Hei. Hay cuatro situaciones: izquierda, izquierda, derecha, izquierda, derecha
            if p == g.left and x == p.left:  # Izquierda izquierda
                # Usa a papá como punto de apoyo
                self.rotateRight(p)
            elif p == g.left and x == p.right:  # Acerca de
                # Usa x como punto de apoyo
                self.rotateLeft(x)
                # Use x como pivote para girar al abuelo a la derecha (la rotación anterior convierte al abuelo en un nuevo padre)
                self.rotateRight(x)
            elif p == g.right and x == p.right:  # Derecha derecha es en realidad la imagen especular de izquierda e izquierda
                # Abuelo zurdo con padre como pivote
                self.rotateLeft(p)
            elif p == g.right and x == p.left:  # Derecha izquierda es en realidad la imagen especular de izquierda y derecha
                # Usa x como punto de apoyo
                self.rotateRight(x)
                # Toma x como punto de apoyo para girar a la izquierda al abuelo (la rotación anterior convierte al abuelo en un nuevo padre)
                self.rotateLeft(x)

    #
    # En cuanto a la rotación de los árboles rojo y negro, siempre ha sido un punto difícil
    # Aquí proporciono una fórmula:
    # Rotación derecha: el fulcro ocupa la posición original del punto de rotación, el punto de rotación derecho del fulcro se usa como el izquierdo y el punto de rotación es el derecho del fulcro
    # Rotación izquierda: el fulcro ocupa la posición original del punto de rotación, el punto de rotación izquierdo del fulcro se usa como el derecho y el punto de rotación es la izquierda del fulcro
    #
    # Pivote p para diestros
    def rotateRight(self, p):
        g = p.parent  # El nodo padre del pivote es el punto de giro
        # Diestro g
        if g == self.root:  # Si g es el nodo raíz, entonces p se convierte en el nodo raíz
            self.root = p
            p.parent = None
        else:  # Si g no es el nodo raíz, entonces debe haber g. El padre p ocupa la posición de g
            gp = g.parent
            p.parent = gp
            if g == gp.left:
                gp.left = p
            else:
                gp.right = p
        g.left = p.right
        if p.right != None:
            p.right.parent = g
        p.right = g
        g.parent = p
        # g y p intercambio de color
        p.color, g.color = g.color, p.color

    # Pivote p para zurdos
    def rotateLeft(self, p):
        g = p.parent  # El nodo padre del pivote es el punto de giro
        # Zurdo g
        if g == self.root:  # Si g es el nodo raíz, entonces p se convierte en el nodo raíz
            self.root = p
            p.parent = None
        else:  # Si g no es el nodo raíz, entonces debe haber g. El padre p ocupa la posición de g
            gp = g.parent
            p.parent = gp
            if g == gp.left:
                gp.left = p
            else:
                gp.right = p
        g.right = p.left
        if p.left != None:
            p.left.parent = g
        p.left = g
        g.parent = p
        # g y p intercambio de color
        p.color, g.color = g.color, p.color


if __name__ == '__main__':
    rbt = RBT()

    datas = [10, 20, 30, 15, 12, 11, 55]

    for dato in datas:
        rbt.add(RBN(dato))

    rbt.midTraverse(rbt.root)

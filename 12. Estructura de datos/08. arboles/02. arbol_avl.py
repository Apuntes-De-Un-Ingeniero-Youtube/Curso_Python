class Node:
    def __init__(self, label):
        self.label = label
        self._parent = None
        self._left = None
        self._right = None
        self.height = 0

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node):
        if node is not None:
            node._parent = self
            self._right = node

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, node):
        if node is not None:
            node._parent = self
            self._left = node

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, node):
        if node is not None:
            self._parent = node
            self.height = self.parent.height + 1
        else:
            self.height = 0


class AVL:

    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, value):
        node = Node(value)

        if self.root is None:
            self.root = node
            self.root.height = 0
            self.size = 1
        else:
            dad_node = None
            curr_node = self.root

            while True:
                if curr_node is not None:

                    dad_node = curr_node

                    if node.label < curr_node.label:
                        curr_node = curr_node.left
                    else:
                        curr_node = curr_node.right
                else:
                    node.height = dad_node.height
                    dad_node.height += 1
                    if node.label < dad_node.label:
                        dad_node.left = node
                    else:
                        dad_node.right = node
                    self.rebalance(node)
                    self.size += 1
                    break

    # Operación de rotación
    def rebalance(self, node):
        n = node

        while n is not None:
            height_right = n.height
            height_left = n.height

            if n.right is not None:
                height_right = n.right.height

            if n.left is not None:
                height_left = n.left.height

            if abs(height_left - height_right) > 1:
                if height_left > height_right:
                    left_child = n.left
                    if left_child is not None:
                        h_right = (left_child.right.height
                                   if (left_child.right is not None) else 0)
                        h_left = (left_child.left.height
                                  if (left_child.left is not None) else 0)
                    if (h_left > h_right):
                        self.rotate_left(n)
                        break
                    else:
                        self.double_rotate_right(n)
                        break
                else:
                    right_child = n.right
                    if right_child is not None:
                        h_right = (right_child.right.height
                                   if (right_child.right is not None) else 0)
                        h_left = (right_child.left.height
                                  if (right_child.left is not None) else 0)
                    if (h_left > h_right):
                        self.double_rotate_left(n)
                        break
                    else:
                        self.rotate_right(n)
                        break
            n = n.parent

    def rotate_left(self, node):
        aux = node.parent.label
        node.parent.label = node.label
        node.parent.right = Node(aux)
        node.parent.right.height = node.parent.height + 1
        node.parent.left = node.right

    def rotate_right(self, node):
        aux = node.parent.label
        node.parent.label = node.label
        node.parent.left = Node(aux)
        node.parent.left.height = node.parent.height + 1
        node.parent.right = node.right

    def double_rotate_left(self, node):
        self.rotate_right(node.getRight().getRight())
        self.rotate_left(node)

    def double_rotate_right(self, node):
        self.rotate_left(node.getLeft().getLeft())
        self.rotate_right(node)

    def empty(self):
        if self.root is None:
            return True
        return False

    def in_order(self, curr_node):
        if curr_node is not None:
            self.in_order(curr_node.left)
            print(curr_node.label, end=" ")
            self.in_order(curr_node.right)

    def pre_order(self, curr_node):
        if curr_node is not None:
            print(curr_node.label, end=" ")
            self.in_order(curr_node.left)
            self.in_order(curr_node.right)

    def pos_order(self, curr_node):
        if curr_node is not None:
            self.in_order(curr_node.left)
            self.in_order(curr_node.right)
            print(curr_node.label, end=" ")

    def get_root(self):
        return self.root


if __name__ == "__main__":

    def menu():
        opc = 0
        arbol_avl = AVL()
        try:
            while opc != 7:
                print("\nÁrbol AVL\n"
                      + "\n\t1. Agregar Nodos"
                      + "\n\t2. ¿Esta vacío el árbol?"
                      + "\n\t3. Recorrer en orden"
                      + "\n\t4. Recorrer en post-orden"
                      + "\n\t5. Recorrer en pre-orden"
                      + "\n\t6. Obtener raiz"
                      + "\n\t7. Salir")

                opc = int(input("Ingrese su opción "))

                if opc == 1:
                    dato = int(input("Ingrese el dato a anexar al arbol "))
                    arbol_avl.insert(dato)
                elif opc == 2:
                    print("SI" if arbol_avl.empty() else "NO")
                elif opc == 3:
                    arbol_avl.in_order(arbol_avl.root)
                elif opc == 4:
                    arbol_avl.pos_order(arbol_avl.root)
                elif opc == 5:
                    arbol_avl.pre_order(arbol_avl.root)
                elif opc == 6:
                    print(arbol_avl.get_root().label)
                elif opc == 7:
                    print("Adios")
                else:
                    print("Ingresaste una opción errónea")
        except Exception as e:
            print("\n Solo se permiten caracteres numéricos")
            print(e)

    menu()

from models.nodo import Node

class LinkedList:
    # constructor
    def __init__(self):
        self.head = None


    # agrego al principio
    def add_first(self,data):
        # agrego el nuevo nodo
        new_node = Node(data)
        # apunto al siguiente nodo
        new_node.next =self.head
        # seteo la raiz del nodo
        self.head = new_node

    # agrego al final
    def add_end(self,data):
        # agrego el nuevo nodo
        new_node = Node(data)
        # hay elemento en la raiz ?
        if not self.head :
            # el elemento se agrega a la raiz
            self.head = new_node
            return
        # creo la variable del ultimo
        last = self.head
        # recorro hasta la ultima posicion
        while last.next:
            last = last.next
        # asigno el nuevo nodo al final
        last.next = new_node

    # eliminar nodo
    def delete_node(self,key):
        # empezar a buscar los nodos
        # miro cual es la cabeza
        current = self.head
        previous = None
        # verifico si hay datos en la raiz y asigno el siguiente nodo a verificar
        while current and current.data != key:
            previous = current
            current = current.next
        # si no existe raiz
        if not current:
            return
        # verifico si no hay elementos previos
        if not previous:
            self.head = current.next
        else:
            # asigno el que sigue del siguiente eliminado para asignar el apuntador
            previous.next = current.next

    # metodo de buscar nodos
    def search(self,key):
        # verifico el nodo actual y lo asigno
        current = self.head
        # recorro con while hasta encontrar el nodo
        while current and current.next != key:
            # si no es el mismo busco en el siguiente
            current = current.next
        # retorno si no esta vacio
        return current is not None
    
    # mostrar la lista
    def show_list(self):
        # defino el nodos como arreglo para guardar de manera temporal
        nodes = []
        current = self.head
        while current:
            nodes.append(current.data)
            # se pasa al siguiente
            current = current.next
        print("Lista: ", nodes)
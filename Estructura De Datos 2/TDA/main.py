from models.listaEnlazada import LinkedList

list = LinkedList()
list.add_first(3)
list.add_first(2)
list.add_first(1)
list.show_list()

list.add_end(4)
list.add_end(5)
list.show_list()

list.delete_node(3)
list.show_list()

print('Buscar el 2: ', list.search(2))
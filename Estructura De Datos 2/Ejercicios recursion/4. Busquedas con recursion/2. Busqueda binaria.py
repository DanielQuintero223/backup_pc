def busqueda_binaria(lista, elemento, inicio=0, fin=None):

    #Si es el primer llamado se calcula el tamanio de la lista
    if fin is None:
        fin = len(lista) - 1
    
    # Caso base: la sublista no tiene elementos
    if inicio > fin:
        return -1
    
    # Calcular el punto medio
    medio = (inicio + fin) // 2
    
    # Caso base: hemos encontrado el elemento
    if lista[medio] == elemento:
        return medio
    
    # Caso recursivo: buscar en la mitad izquierda, por eso el -1 
    # para que se mueva una posicion a la izquierda
    elif lista[medio] > elemento:
        return busqueda_binaria(lista, elemento, inicio, medio - 1)
    
    # Caso recursivo: buscar en la mitad derecha, por eso el +1 
    # para que se mueva una posicion a la derecha
    else:
        return busqueda_binaria(lista, elemento, medio + 1, fin)

# Ejemplo de uso
lista_ordenada = [1, 2, 3, 4, 5, 6, 7, 8, 9]
elemento = 8
resultado = busqueda_binaria(lista_ordenada, elemento)
print("El elemento " + str(elemento) + " se encuentra en el índice " + str(resultado))

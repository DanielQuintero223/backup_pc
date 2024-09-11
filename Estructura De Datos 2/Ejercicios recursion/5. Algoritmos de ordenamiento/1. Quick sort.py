def quick_sort(lista):
    # Caso base: una lista de tamaño 0 o 1 ya está ordenada
    if len(lista) <= 1:
        return lista
    
    # Elegir el pivote (usamos el último elemento en este caso)
    pivote = lista[-1]
    menores = []
    iguales = []
    mayores = []
    
    # Particionar la lista
    for x in lista:
        if x < pivote:
            menores.append(x)
        elif x == pivote:
            iguales.append(x)
        else:
            mayores.append(x)
    
    # Ordenar recursivamente y combinar (El que se tomo como pivote y sus iguales se excluyen del ordenamiento)
    return quick_sort(menores) + iguales + quick_sort(mayores)

# Ejemplo de uso
lista = [38, 27, 43, 3, 9, 82, 10]
print("Lista original:", lista)
lista_ordenada = quick_sort(lista)
print("Lista ordenada:", lista_ordenada)

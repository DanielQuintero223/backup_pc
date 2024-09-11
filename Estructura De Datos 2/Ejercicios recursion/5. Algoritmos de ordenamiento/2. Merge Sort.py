def merge_sort(lista):
    # Caso base: una lista de tamaño 0 o 1 ya está ordenada
    if len(lista) <= 1:
        return lista
    

    #Paso 1: El primer paso es dividir la lista en dos mitades. Esto se hace recursivamente 
    # hasta que cada sublista tenga un tamaño de 1 (o 0), porque una lista de 
    # tamaño 1 ya está ordenada.
    
    # Dividir la lista en mitades
    medio = len(lista) // 2
    izquierda = lista[:medio]
    derecha = lista[medio:]
    
    # Paso 2: Una vez que hemos dividido la lista en sublistas de tamaño 1, comenzamos a mezclar estas sublistas. 
    # Pero antes de mezclar, necesitamos asegurarnos de que cada mitad está ordenada. 
    # Aquí es donde la recursión entra en juego: aplicamos Merge Sort recursivamente en cada mitad.

    # Ordenar recursivamente cada mitad
    izquierda = merge_sort(izquierda)
    derecha = merge_sort(derecha)    


    #Paso 3: El último paso es combinar (mezclar) las sublistas ordenadas en una sola lista ordenada. 
    # Esto se hace comparando los elementos de las sublistas y agregándolos en el orden correcto a una nueva lista.
    
    # Mezclar las mitades ordenadas
    return mezclar(izquierda, derecha)


def mezclar(izquierda, derecha):
    resultado = []
    i = j = 0
    # Combinar las dos mitades ordenadas
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    
    # Agregar los elementos restantes que no se hayan podido comparar, ya 
    # que no necesariamente las listas derecha - izquierda tienen el mismo tamaño
    resultado.extend(izquierda[i:]) #De la posicion i en adelante (Es decir los ultimos)
    resultado.extend(derecha[j:])#De la posicion j en adelante (Es decir los ultimos)
    
    return resultado

# Ejemplo de uso
lista = [38, 27, 43, 3, 9, 82, 10]
print("Lista original:", lista)
lista_ordenada = merge_sort(lista)
print("Lista ordenada:", lista_ordenada)

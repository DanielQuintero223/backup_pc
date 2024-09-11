def busqueda_lineal(lista, elemento, indice=0):
    # Caso base: hemos llegado al final de la lista sin encontrar el elemento
    if indice >= len(lista):
        return -1
    
    # Caso base: hemos encontrado el elemento
    if lista[indice] == elemento:
        return indice
    
    # Caso recursivo: seguir buscando en el resto de la lista
    return busqueda_lineal(lista, elemento, indice + 1)

# Ejemplo de uso
lista = [4, 2, 7, 1, 3, 5]
elemento = 3
resultado = busqueda_lineal(lista, elemento)
print("El elemento "+ str(elemento) + " se encuentra en el índice " + str(resultado))

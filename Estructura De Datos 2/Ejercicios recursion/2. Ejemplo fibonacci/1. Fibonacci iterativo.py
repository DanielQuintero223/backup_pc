def fibonacci_iterativo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    #a, b = 0, 1
    a = 0
    b = 1
    #Como solo requerimos es la ejecucion del ciclo, no es necesario establecer variable de control, por eso el _
    for _ in range(2, n + 1):
        #a, b = b, a + b
        temporal = a #almacenamos el valor anterior de a
        a = b # a toma el valor de b
        b = temporal + b # b es igual al anterior valor de a + el valor de b
                
    return b

# Ejemplo de uso
print(fibonacci_iterativo(6))  # Salida: 8
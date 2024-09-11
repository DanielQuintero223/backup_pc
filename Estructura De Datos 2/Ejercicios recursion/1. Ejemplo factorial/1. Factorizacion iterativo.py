def factorial_iterativo(n):
    resultado = 1
    #El range se detiene antes del numero especificado, por ende debe ser n+1
    for i in range(1, n + 1):
        print("resultado =" + str(resultado) + "*" + str(i))
        resultado *= i 
    return resultado

print("El resultado es " + str(factorial_iterativo(4)))  

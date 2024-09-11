def factorial_recursivo(n):
    if n == 0:
        return 1  # Caso base
    else:
        print (f"{n} X factorial_recursivo({(n-1)})") 
        return n * factorial_recursivo(n - 1)  # Llamada recursiva


print(factorial_recursivo(5)) 



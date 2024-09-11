def fibonacci_recursivo(n):
    if n == 0:
        return 0  # Caso base
    elif n == 1:
        return 1  # Caso base
    else:        
         # Llamada recursiva
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2) 

print(fibonacci_recursivo(6)) 
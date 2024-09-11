#Directa: Calculo del factorial o la serie fibonacci (Ocurre cuando una función se llama a sí misma directamente.)

"""
def factorial(n):
    if n == 0:
        return 1  # Caso base
    else:
        return n * factorial(n - 1)  # Llamada recursiva directa

print(factorial(3))
"""

#Recursividad indirecta: Dado un numero N, imprimir desde dicho numero hasta 1, marcando dicho primer numero con A, el siguiente con 
#B y asi sucesivamente hasta 1 (Ocurre cuando una función A llama a otra función B, y B eventualmente llama a la función A.)

"""
def funcion_a(n):
    if n > 0:
        print("A", n)
        funcion_b(n - 1)

def funcion_b(n):
    if n > 0:
        print("B", n)
        funcion_a(n - 1)

funcion_a(5)
"""


#Recursividad lineal: Una cuenta regresiva (La función se llama a sí misma una sola vez por invocación 
# (Subtipo de recursividad directa, por ejemplo, aquí el factorial seria directa y lineal, mientras 
# que Fibonacci es directa mas no lineal, ya que tiene más de un llamado por invocación).)

"""
def cuenta_regresiva(n):
    if n > 0:
        print(n)
        cuenta_regresiva(n - 1)
    else:
        print("¡Despegue!")

cuenta_regresiva(10)
"""



# Recursividad multiple: Serie fibonacci (La función se llama a sí misma más de una vez por invocación)

"""
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Llamada recursiva múltiple

print(fibonacci(5))
"""
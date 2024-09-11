# iterable[inicio:fin:paso]


# función recursiva que tome una cadena de caracteres y la invierta.
# inicializo la cadena de caracteres
cadena = "Hola Mundo"

def invertir(cadena):
    # caso base
    if len(cadena) == 0:
        return cadena
    else:
        # caso recursivo
        # llamo de nuevo el metodo con la cadena sin el primer caracter{1:} y le agrego el primer caracter{0}
        return invertir(cadena[1:]) + cadena[0]
    
print(invertir(cadena))

print('------------------------------------------')

# una función recursiva que calcule la suma de los dígitos de un número entero positivo.
# inicializo el número
numero = 1234

def suma_digitos(numero):
    # caso base
    if numero == 0:
        return 0
    else:
        # caso recursivo
        # saco el residuo del numero {numero % 10} y llamo a la función con el número sin el último dígito {numero // 10}
        return numero % 10 + suma_digitos(numero // 10)
    
# imprimo la suma de los dígitos del número
print(suma_digitos(numero))

print('------------------------------------------')

# función recursiva que verifique si una cadena es un palíndromo

cadena = "radar"

def palindromo(cadena):
    # caso base
    if len(cadena) == 0 or len(cadena) == 1:
        return True
    else:
        # caso recursivo
        # si la cadena es un palíndromo, la primera y última letra deben ser iguales
        if cadena[0] == cadena[-1]:
            return palindromo(cadena[1:-1])
        else:
            return False

# imprimo si la cadena es un palíndromo
print(palindromo(cadena))

print('------------------------------------------')

# función recursiva que tome una lista y la invierta y retonor una lista invertida
# inicializo la lista
lista = [1, 2, 3, 4, 5]
invertida = []

def invertir_lista(lista):
    # caso base
    if len(lista) == 0:
        return invertida
    else:
        # caso recursivo
        # agrego el último elemento de la lista a la lista invertida
        invertida.append(lista[-1])
        # llamo el metodo recursivo del final hacia atras hasta cumplir el caso base
        return invertir_lista(lista[:-1])
    

# imprimo la lista invertida
print(invertir_lista(lista))


print('------------------------------------------')










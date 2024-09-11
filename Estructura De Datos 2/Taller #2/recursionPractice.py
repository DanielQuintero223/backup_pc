# contas cantidad de digitos de manera recursiva
num = 4220103

def cantDig(num):
    # caso base 
    if num == 0:
        return 0
    else:
        # caso recursivo
        # sumo 1 y llamo a la función con el número y lo divido entre 10 para sacar el ultimo digito y seguir contando
        return 1 + cantDig(num // 10)
    
print(cantDig(num))

print('------------------------------------------')

# numero de veces que aparece un digito en un número

num2 = 2234567
dig2 = 2

def browseDig(num, dig):
    # caso base
    if num == 0:
        return 0
    else:
        # caso recursivo
        # si el digito es igual al último digito del número, sumo 1 y llamo a la función con el número y lo divido entre 10 para sacar el último digito
        if num % 10 == dig:
            return 1 + browseDig(num // 10, dig)
        else:
            # si no es igual, solo llamo a la función con el número y lo divido entre 10 para sacar el último digito
            print(num)
            return browseDig(num // 10, dig)
        
print(browseDig(num2, dig2))

print('------------------------------------------')

# invertir un número

num3 = 4321231

def invertDig(num):
    # caso base
    if num == 0:
        return 0
    else:
        # caso recursivo
        # imprimo el último dígito del número y llamo a la función con el número y lo divido entre 10 para sacar el último dígito
        print(num % 10, end='')
        return invertDig(num // 10)
    

print(invertDig(num3))


print('------------------------------------------')

# digitos pares

num4 = 12345

def digPar(num):
    # caso base
    if num == 0:
        return 0
    else:
        # si la division consecutiva del numero entre 2 da 0 es porque el numero es par
        if num % 2 == 0:
            return 1 + (digPar(num // 10))
        else:
            # si no se da el caso de arriba entonces solo quito el ultimo digito
            return (digPar(num // 10))
        

print(digPar(num4))

print('------------------------------------------')

# cual es el numero mas pequeño de una lista

lista = [ 12, 3, 4, 5, 6, 7, 8, 9]

def minNum(lista):
    # caso base
    if len(lista) == 1:
        return lista[0]
    else:
        # caso recursivo
        # si el primer número de la lista es menor al segundo, lo elimino de la lista y llamo a la función con la lista
        if lista[0] < lista[1]:
            lista.pop(1)
            return minNum(lista)
        else:
            # si no, elimino el primer número de la lista y llamo a la función con la lista
            lista.pop(0)
            return minNum(lista)
        
print(minNum(lista))


print('------------------------------------------')
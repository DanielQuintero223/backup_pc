print("*****************************")
print("*******EJERICIO 1************")
print("*****************************")

"""
def presentacion():
    print("Programa que permite cargar dos valores por teclado.")
    print("*******************************")


def carga_suma():
    valor1=int(input("Ingrese el primer valor:"))
    valor2=int(input("Ingrese el segundo valor:"))
    suma=valor1+valor2
    print("La suma de los dos valores es:",suma)


def finalizacion():
    print("*******************************")    
    print("Gracias por utilizar este programa")


# programa principal

presentacion()
carga_suma()
finalizacion()
"""




print("*****************************")
print("*******EJERICIO 2************")
print("*****************************")


"""
Solicite la carga de dos valores enteros y muestre su suma.
Repetir la carga e impresion de la suma 5 veces.
"""

"""
def carga_suma():
    valor1=int(input("Ingrese el primer valor:"))
    valor2=int(input("Ingrese el segundo valor:"))
    suma=valor1+valor2
    print("La suma de los dos valores es:",suma)


def separacion():
    print("*******************************")    


# programa principal

for x in range(5):
    carga_suma()
    separacion()
"""




print("*****************************")
print("*******EJERICIO 3************")
print("*****************************")


"""
Implementar una función que reciba tres enteros y muestre el mayor de ellos. La carga de los valores hacerlo por teclado.
"""

"""
def mostrar_mayor(v1,v2,v3):
    print("El valor mayor de los tres numeros es")
    if v1>v2 and v1>v3:
        print(v1)
    else:
        if v2>v3:
            print(v2)
        else:
            print(v3)


def cargar():
    valor1=int(input("Ingrese el primer valor:"))
    valor2=int(input("Ingrese el segundo valor:"))
    valor3=int(input("Ingrese el tercer valor:"))
    mostrar_mayor(valor1,valor2,valor3)


# programa principal

cargar()
"""





print("*****************************")
print("*******EJERICIO 4************")
print("*****************************")


"""
FUNCION CON RETORNO DE DATOS: función que recibe como parámetro el valor del lado de un cuadrado y nos retorne su superficie.
"""

"""
def retornar_superficie(lado):
    sup=lado*lado
    return sup


# bloque principal del programa

va=int(input("Ingrese el valor del lado del cuafrado:"))
superficie=retornar_superficie(va)
print("La superficie del cuadrado es",superficie)
"""



print("*****************************")
print("*******EJERICIO 5************")
print("*****************************")

"""
EJERCICIO CON arregloS Y FUNCIONES
"""

"""
def sumarizar(arreglo):
    suma=0
    for x in range(len(arreglo)):
        suma=suma+arreglo[x]
    return suma


def mayor(arreglo):
    may=arreglo[0]
    for x in range(1,len(arreglo)):
        if arreglo[x]>may:
            may=arreglo[x]
    return may


def menor(arreglo):
    men=arreglo[0]
    for x in range(1,len(arreglo)):
        if arreglo[x]<men:
            men=arreglo[x]
    return men
    

# bloque principal del programa

arreglovalores=[10, 56, 23, 120, 94]
print("La arreglo completa es")
print(arreglovalores)
print("La suma de todos su elementos es", sumarizar(arreglovalores))
print("El mayor valor de la arreglo es", mayor(arreglovalores))
print("El menor valor de la arreglo es", menor(arreglovalores))
"""



print("*****************************")
print("*******EJERICIO 6************")
print("*****************************")

"""
Implementar una función que cargue por teclado una lista de 5 enteros y la retorne. 
Una segunda función debe recibir un arreglo y mostrar todos los valores mayores a 10. 
Desde el bloque principal del programa llamar a ambas funciones.
"""

"""
def carga_lista():
    li=[]
    for x in range(5):
        valor=int(input("Ingrese valor:"))
        li.append(valor)
    return li


def imprimir_mayor10(li):
    print("Elementos de la lista mayores a 10")
    for x in range(len(li)):
        if li[x]>10:
            print(li[x])


# bloque principal del programa

lista=carga_lista()
imprimir_mayor10(lista)
"""



print("*****************************")
print("*******EJERICIO 7************")
print("*****************************")

"""
Retorno simultaneo de multiples valores: Desarrollar un programa que permita cargar 5 nombres de personas y sus edades respectivas. 
Luego de realizar la carga por teclado de todos los datos imprimir los nombres de las personas mayores de edad (mayores o iguales a 18 años)
Imprimir la edad promedio de las personas.
"""

"""
def cargar_datos():
    nom=[]
    ed=[]
    for x in range(5):
        v1=input("Ingrese el nombre de la persona:")
        nom.append(v1)
        v2=int(input("Ingrese la edad:"))
        ed.append(v2)
    return [nom,ed]


def mayores_edad(nom,ed):
    print("Nombres de personas mayores de edad")
    for x in range(len(nom)):
        if ed[x]>=18:
            print(nom[x])


def promedio_edades(ed):
    suma=0
    for x in range(len(ed)):
        suma=suma+ed[x]
    promedio=suma//5
    print("Edad promedio de las personas:",promedio)
    

# bloque principal

nombres,edades=cargar_datos()
mayores_edad(nombres,edades)
promedio_edades(edades)          
"""




print("*****************************")
print("*******EJERICIO 8************")
print("*****************************")

"""
Parametros opcionales y valores por defecto: Repite caracter segun el texto ingresado
"""

"""
def titulo_subrayado(titulo,caracter="*"):
    print(titulo)
    print(caracter*len(titulo))


# bloque principal

titulo_subrayado("Sistema de Administracion")
titulo_subrayado("Ventas","-")
"""


print("*****************************")
print("*******EJERICIO 9************")
print("*****************************")


"""
Parametros dinamicos. Para un parametro dinamico se le antecede un *
"""

"""
def sumar(v1,v2,*lista):
    suma=v1+v2
    for x in range(len(lista)):
        suma=suma+lista[x]
    return suma


# bloque principal

print("La suma de 1+2")
print(sumar(1,2))
print("La suma de 1+2+3+4")
print(sumar(1,2,3,4))
print("La suma de 1+2+3+4+5+6+7+8+9+10")
print(sumar(1,2,3,4,5,6,7,8,9,10))
"""


print("*****************************")
print("*******EJERICIO 10***********")
print("*****************************")

"""
Desempaquetar una lista en N variables de un metodo. Para esto se le antecede un * a la lista
que se manda por parametro
"""

""" def sumar(v1, v2, v3):
    return v1 + v2 + v3

li=[2, 4, 5]
su=sumar(*li)
print(su)
 """


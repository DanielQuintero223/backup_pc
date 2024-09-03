
print("*****************************")
print("*******EJERICIO 01***********")
print("*****************************")

"""
TUPLAS: Una tupla permite almacenar una colección de datos no 
necesariamente del mismo tipo. Los datos de la tupla son inmutables 
a diferencia de las listas que son mutables.
"""

"""CREACION DE UNA TUPLA"""

""" x=10
y=30
punto=x,y
print(punto) """

"""DESEMPAQUETANDO UNA TUPLA"""

""" fecha=(25, "diciembre", 2016)
print(fecha)
dd,mm,aa=fecha
print("Dia",dd)
print("Mes",mm)
print("Año",aa) """


"""TUPLAS V2"""
mi_tupla = (1,2,3)
print(f"Primer valor {mi_tupla[0]} --- Segundo valor {mi_tupla[1]} --- Tercer valor {mi_tupla[2]}")



print("*****************************")
print("*******EJERICIO 02***********")
print("*****************************")


"""
FOR EACH EN PYTHON
"""

""" 
#Esto es un comentario de linea
lista=[2, 3, 50, 7, 9]

for elemento in lista:
    print(elemento)  """



print("*****************************")
print("*******EJERICIO 03***********")
print("*****************************")


"""
DATOS DE TIPO DICCIONARIO
"""

"""
productos={"manzanas":39, "peras":32, "lechuga":17}
print(productos)
"""

""" 
def imprimir(paises):
    for clave in paises:
        print(clave,'-',paises[clave])


# bloque principal

paises={"argentina":40000000, "españa":46000000, "brasil":190000000, "uruguay": 3400000}
imprimir(paises) """





print("*****************************")
print("*******EJERICIO 04***********")
print("*****************************")

"""
Desarrollar una aplicación que nos permita crear un 
diccionario ingles/español. La clave es la 
palabra en ingles y el valor es la palabra en español.
"""

""" 
def cargar():
    #Se define la estructura de tipo diccionario
    diccionario={}
    #Bandera para detener el ingreso de datos
    continuar="s"
    while continuar=="s":
        espanol=input("Ingrese palabra en español:")
        ingles=input("Ingrese palabra en ingles:")
        diccionario[ingles]=espanol
        continuar=input("Quiere cargar otra palabra:[s/n]")
    return diccionario


def imprimir(diccionario):
    print("Listado completo del diccionario")
    for ingles in diccionario:
        print(ingles,'-',diccionario[ingles])


def consulta_palabra(diccionario):
    pal=input("Ingrese la palabra en ingles a consultar:")
    if pal in diccionario:
        print("En español significa:",diccionario[pal])


# bloque principal

#Se define el diccionario con las palabras
diccionario=cargar()
#Se recorre el diccionario y se imprime
imprimir(diccionario)
#Se consulta en el diccionario si existe una palabra en particular
consulta_palabra(diccionario) """




print("*****************************")
print("*******EJERICIO 05***********")
print("*****************************")

"""
IMPORTAR BIBLIOTECAS
"""

""" 
import random

def cargar():
    lista=[]
    for x in range(10):
        lista.append(random.randint(0,1000))
    return lista

def imprimir(lista):
    print(lista)    

def mezclar(lista):
    random.shuffle(lista)
  
# bloque principal

lista=cargar()
print("Lista generada aleatoriamente")
imprimir(lista)
mezclar(lista)
print("La misma lista luego de mezclar")
imprimir(lista) """
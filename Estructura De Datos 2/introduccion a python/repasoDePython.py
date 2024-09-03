# lado = int(input("Ingrese el lado del cuadrado: "))
# area = lado * lado
# print("El area del cuadrado es: ", area)


# precio = float(input("Ingrese el precio del producto: "))
# cantidad = int(input("Ingrese la cantidad de productos: "))
# importe = precio * cantidad

# # seteo de decimales
# print("El importe a pagar es: ", str(importe))

# # condicionales con ingreso de datos
# num1 = int(input("Ingrese el primer numero: "))
# num2 = int(input("Ingrese el segundo numero: "))
# if num1 > num2:
#     print("El numero mayor es: ", num1)
# else:
#     print("El numero mayor es: ", num2)

# nota1 = float(input("Ingrese la nota 1: "))
# nota2 = float(input("Ingrese la nota 2: "))
# nota3 = float(input("Ingrese la nota 3: "))
# promedio = (nota1 + nota2 + nota3) / 3
# print("El promedio es: ", str(promedio))

# #condicionales
# if promedio >= 4.0:
#     print("Promocionado")
# else:
#     if promedio >= 3.0:
#         print("Regular")
#     else:
#         print("Reprobado")


# # for por rangos
# for i in range(20, 31,2):
#     print(i)


# # sumatoria
# suma = 0
# promedio = 0
# for i in range(10):
#     valor = int(input("Ingrese un valor: "))
#     suma = suma + valor
# print("La suma de los valores ingresados es: ", suma)
# promedio = suma / 10
# print("El promedio de los valores ingresados es: ", promedio)

# VERIIFICAR CORREO
# correo = input("Ingrese su correo: ")
# cantidad = 0
# x= 0
# while x<len(correo):
#     if correo[x] == "@":
#         cantidad = cantidad + 1
#     x = x + 1
# if cantidad == 1:
#     print("Correo correcto")
# else:
#     print("Correo incorrecto")

# funciones upper lower capitalize
# nombre= 'DANiel'
# print(nombre.upper())
# print(nombre.lower())
# print(nombre.capitalize())


arreglo1 = [1,2,3,4,5,6,7,8,9,10]
print(arreglo1)
arreglo1.append('daniel')
print(arreglo1)
# insertacion de datos en una posicion especifica
arreglo1.insert(2, 77)
print(arreglo1)


# creacion de arreglos de arreglos
arreglo = [[1,2,3],[4,5,6],[7,8,9]]

# imprime el arreglo de arreglos completo
print(arreglo)

# imprime el primer arreglo
print(arreglo[0])

# imprime el primer elemento del primer arreglo
print(arreglo[0][0])

# recorro el primer arreglo de arreglos
for i in arreglo[0]:
    print(i)

# recorro el arreglo de arreglos
print("Recorrido completo")
for i in arreglo:
    for j in i:
        print(j)
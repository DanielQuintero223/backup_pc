#El import cambia, siendo from el archivo y el import la clase
from empleado import Empleado

# bloque principal

nombre = input("Ingrese el nombre del empleado:")
sueldo = float(input("Ingrese el sueldo:"))

empleado1 = Empleado(nombre, sueldo)
empleado1.imprimir()
empleado1.paga_impuestos()
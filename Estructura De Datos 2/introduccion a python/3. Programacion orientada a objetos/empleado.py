class Empleado:
    #Deficion del constructor, es con doble guion bajo al inicio y al final
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

    def imprimir(self):
        print("Nombre:", self.nombre)
        print("Sueldo:", self.sueldo)

    def paga_impuestos(self):
        if self.sueldo > 3000:
            print("Debe pagar impuestos")
        else:
            print("No paga impuestos")

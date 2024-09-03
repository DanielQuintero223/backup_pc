class Persona:

    def __init__(self):
        self.nombre=input("Ingrese el nombre:")
        self.edad=int(input("Ingrese la edad:"))

    def getInfo(self):
        print("Nombre:",self.nombre)
        print("Edad:",self.edad)
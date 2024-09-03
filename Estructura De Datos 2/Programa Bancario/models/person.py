class Person:

    def __init__(self):
        self.name=input("Ingrese el nombre:")
        self.lastName=input("Ingrese el apellido:")
        self.identification=input("Ingrese la identificacion:")
        self.age=int(input("Ingrese la edad:"))
    
    def showPerson(self):
        print("Nombre:",self.name)
        print("Apellido:",self.lastName)
        print("Identificacion:",self.identification)
        print("Edad:",self.age)
class Operacion:

    def __init__(self, num1, num2):
        self.lista=[]
        self.lista.append(num1)
        self.lista.append(num2)
        self.sumar()
        
    def sumar(self):
        suma=self.lista[0]+self.lista[1]
        print("La suma es",suma)




# bloque principal

num1 = int(input("Ingrese primer valor:"))
num2 = int(input("Ingrese segundo valor:"))

operacion1=Operacion(num1,num2)
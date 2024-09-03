class Cliente:

    """ Variable  estatica compartida por todos los miembros de la clase."""
    suspendidos=[]
    iva=19

    def __init__(self,codigo,nombre):
        self.codigo=codigo
        self.nombre=nombre

    def imprimir(self):
        print("Codigo:",self.codigo)
        print("Nombre:",self.nombre)

        """ Imprimir variable local """
        """ print("IVA:",self.iva) """

        """ imprimir variable estatica """
        print("IVA:",Cliente.iva)

        self.esta_suspendido()

    def esta_suspendido(self):
        if self.codigo in Cliente.suspendidos:
            print("Esta suspendido")
        else:
            print("No esta suspendido")
        print("_____________________________")

    def suspender(self):
        Cliente.suspendidos.append(self.codigo)
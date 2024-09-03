from models.client import Client
# importo la clase cliente para generar despues una lista de clientes

class Bank:

    # creo la clase banco con sus variables
    def __init__(self):
        self.name=input("Ingrese el name del banco:")
        self.city=input("Ingrese la city:")
        self.clients=[]
    
    # creo un metodo para crear un cliente
    def createClient(self):
        cliente=Client()
        return cliente
    # creo un metodo para mostrar el banco
    def showBank(self):
        print("name del banco:",self.name)
        print("city:",self.city)
    # creo un metodo para mostrar los clients
    def showClients(self):
        for i in self.clients:
            i.showClient()
    # creo un metodo para consignar dinero
    def deposit(self,clientB,amount):
        for i in self.clients:
            if i.identification==clientB:
                i.credit+=amount

    # creo un metodo para retirar dinero
    def withdraw(self,clientB,amount):
        for i in self.clients:
            if i.identification==clientB:
                i.credit-=amount

    # creo un metodo para consultar saldo
    def showBalance(self,clientB):
        for i in self.clients:
            if i.identification==clientB:
                i.showClient()
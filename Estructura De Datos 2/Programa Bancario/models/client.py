from models.person import Person
## importo la super clase person para generar una herencia en esta clase

class Client(Person):

# creo el constructor heredando de la clase Person
    def __init__(self):
        super().__init__()
        self.credit=float(input("Ingrese el credito:"))
    
    def showClient(self):
        print("Cliente:")
        super().showPerson()
        print("Credito:",self.credit)
        print("------------------------------------")
    
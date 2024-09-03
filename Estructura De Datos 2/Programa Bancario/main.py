from models.bank import Bank

print("------------------------------------")
print("Bienvenido al sistema bancario")
print("Que operacion desea realizar?")
# creo un switch con las opciones que el usuario puede realizar
print("1.- Crear un banco")
print("2.- Crear un cliente")
print("3.- Mostrar bancos")
print("4.- Mostrar clientes")
print("5.- Consignar dinero")
print("6.- Retirar dinero")
print("7.- consultar saldo")
print("8.- Salir")
opcion=int(input("Ingrese la opcion:"))
# creo un ciclo para que el usuario pueda realizar varias operaciones
while opcion!=8:
    if opcion==1:
        banco=Bank()
        print("Banco creado")
    elif opcion==2:
        banco.clients.append(banco.createClient())
        print("Cliente creado")
    elif opcion==3:
        banco.showBank()
    elif opcion==4:
        banco.showClients()
    elif opcion==5:
        clientBrowser=input("Ingrese la identificacion del cliente:")
        amount=int(input("Ingrese la cantidad a consignar:"))
        banco.deposit(clientBrowser,amount)
        print("Consignacion realizada")
    elif opcion==6:
        clientBrowser=input("Ingrese la identificacion del cliente:")
        amount=int(input("Ingrese la cantidad a retirar:"))
        banco.withdraw(clientBrowser,amount)
        print("Retiro realizado")
    elif opcion==7:
        clientBrowser=input("Ingrese la identificacion del cliente:")
        banco.showBalance(clientBrowser)
    else:
        print("Opcion invalida")
    print("------------------------------------")
    print("Que operacion desea realizar?")
    print("1.- Crear un banco")
    print("2.- Crear un cliente")
    print("3.- Mostrar bancos")
    print("4.- Mostrar clientes")
    print("5.- Consignar dinero")
    print("6.- Retirar dinero")
    print("7.- consultar saldo")
    print("8.- Salir")
    opcion=int(input("Ingrese la opcion:"))
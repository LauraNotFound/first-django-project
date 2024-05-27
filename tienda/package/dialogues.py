from .entitiesClient import *
from .entitiesSale import *
from .entitiesVehicles import *
from .validations import *

#VEHICLE
managerVehicle = VehicleManager()

def appendAVehicle():
    print("Registrar un vehiculo")
    serie = read_text("Serie: ")
    brand = read_text("Brand: ")
    model = read_text("Model: ")
    amount = read_float("Amount: ")
    managerVehicle.appendVehicle(serie, brand, model, amount)
    print()
    MenuVehicle()

def upAVehicle():
    print("Modificar un vehiculo")
    id = read_int("ID: ")
    serie = read_text("Serie: ")
    brand = read_text("Brand: ")
    model = read_text("Model: ")
    amount = read_float("Amount: ")
    managerVehicle.upVehicle(id, serie or None, brand or None, model or None, amount or None)
    print()
    MenuVehicle()

def deleteAVehicle():
    print("Eliminar un vehiculo")
    id = read_int("ID: ")
    managerVehicle.deleteVehicle(id)
    print()
    MenuVehicle()

def showAllVehicles():
    managerVehicle.showVehicles()
    print()
    MenuVehicle()
           
def MenuVehicle():
    print("Menú de control de Vehiculos")
    print("1. Agregar vehiculo")
    print("2. Modificar vehiculo")
    print("3. Eliminar vehiculo")
    print("4. Mostrar vehiculos")
    print("5. Regresar al menú anterior")
    print("6. Salir")
    opc = read_int("Ingrese la opción: ")
    if opc == 1:
        appendAVehicle()
    else: 
        if opc == 2:
            upAVehicle()
        else:
            if opc == 3:
                deleteAVehicle()
            else: 
                if opc == 4:
                    showAllVehicles()
                else:
                    if opc == 5:
                        Menu()
                    else:
                        exit() 

#SALE

managerSale = SaleManager()
def appendASale():
    print("Registra una venta")
    idVehicle = read_int("ID vehicle: ")
    idClient = read_int("ID client: ")
    amount = read_float("Amount: ")
    managerSale.appendSale(idVehicle, idClient, amount)
    print()
    MenuSale()

def upASale():
    print("Modificar una venta")
    idVehicle = read_int("ID vehicle: ")
    idClient = read_int("ID client: ")
    amount = read_float("Amount: ")
    managerSale.upSale(id, idVehicle or None, idClient or None, amount)
    print()
    MenuSale()

def deleteASale():
    print("Eliminar una venta")
    id = read_int("ID: ")
    managerSale.deleteSale(id)
    print()
    MenuSale()

def showAllSales():
    managerSale.showSales()
    print()
    MenuSale()
           
def MenuSale():
    print("Menú de control de ventas")
    print("1. Agregar venta")
    print("2. Modificar venta")
    print("3. Eliminar venta")
    print("4. Mostrar ventas")
    print("5. Regresar al menú anterior")
    print("6. Salir")
    opc = read_int("Ingrese la opción: ")
    if opc == 1:
        appendASale()
    else: 
        if opc == 2:
            upASale()
        else:
            if opc == 3:
                deleteASale()
            else: 
                if opc == 4:
                    showAllSales()
                else:
                    if opc == 5:
                        Menu()
                    else:
                        exit()

#CLIENT
managerClient = ClientManager()
def appendAClient():
    print("Registra un cliente")
    name = read_text("Name: ")
    lastName = read_text("LastName: ")
    numberVehicles = read_int("Cantidad de Vehículos: ")
    managerClient.appendClient(name, lastName, numberVehicles)
    print()
    MenuClient()

def upAClient():
    print("Modificar un cliente")
    id = read_int("ID: ")
    name = read_text("Name: ")
    lastName = read_text("LastName: ")
    numberVehicles = read_int("Cantidad de Vehículos: ")
    numberVehicles = numberVehicles if numberVehicles else None
    managerClient.upClient(id, name or None, lastName or None, numberVehicles)
    print()
    MenuClient()

def deleteAClient():
    print("Eliminar un cliente")
    id = read_int("ID: ")
    managerClient.deleteClient(id)
    print()
    MenuClient()

def showAllClients():
    managerClient.showClients()
    print()
    MenuClient()
           
def MenuClient():
    print("Menú de control de Clientes")
    print("1. Agregar cliente")
    print("2. Modificar cliente")
    print("3. Eliminar cliente")
    print("4. Mostrar clientes")
    print("5. Regresar al menú anterior")
    print("6. Salir")
    opc = read_int("Ingrese la opción: ")
    if opc == 1:
        appendAClient()
    else: 
        if opc == 2:
            upAClient()
        else:
            if opc == 3:
                deleteAClient()
            else: 
                if opc == 4:
                    showAllClients()
                else:
                    if opc == 5:
                        Menu()
                    else:
                        exit()

# MENÚ GENERAL 
def Menu():
    print("Lista de opciones: \n1. Vehículo\n2. Venta\n3. Cliente")
    opc = read_int("Ingrese la opción: ")
    if opc == 1:
        MenuVehicle()
    else: 
        if opc == 2:
            MenuSale()
        else:
            if opc == 3:
                MenuClient()
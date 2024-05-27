class Sale:
    def __init__(self, idClient, idVehicle, amount):
        self._idClient = idClient
        self._idVehicle = idVehicle
        self._amount = amount
    
    @property
    def idClient(self):
        return self._idClient
    
    @idClient.setter
    def idClient(self, value):
        self._idClient = value
    
    @property
    def idVehicle(self):
        return self._idVehicle
    
    @idVehicle.setter
    def idVehicle(self, value):
        self._idVehicle = value

    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def amount(self, value):
        self._amount = value  

class SaleManager:
    def __init__(self):
        self._sales = []
        self._idSale = 1
    
    def appendSale(self, idClient, idVehicle, amount):
        sale  = Sale(idClient, idVehicle, amount)
        self._sales.append({"id": self._idSale, "sale": sale})
        self._idSale += 1
        print("Venta agregada exitosamente!")
    
    def showSales(self):
        if not self._sales:
            print("No hay ventas registradas")
        else:
            for entry in self._sales:
                sale = entry["sale"]
                print(f"ID: {entry['id']}, ID Client: {sale.idClient}, ID Vehicle: {sale.idVehicle}, Amount: {sale.amount}")
    
    def upSale(self, id, idClient=None, idVehicle=None, amount=None):
        for entry in self._sales:
            if entry["id"] == id:
                sale = entry["sale"]
                if idClient is not None:
                    sale.idClient = idClient
                if idVehicle is not None:
                    sale.idVehicle = idVehicle
                if amount is not None:
                    sale.amount = amount
                print("Venta modificada exitosamente!")
                return
        print("Venta no encontrada")
    
    def deleteSale(self, id):
        for entry in self._sales:
            if entry["id"] == id:
                self._sales.remove(entry)
                print("Venta eliminada exitosamente!")
                return
        print("Venta no encontrada")
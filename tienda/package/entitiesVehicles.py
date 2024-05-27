class Vehicle:
    def __init__(self, serie, brand, model, amount):
        self._serie = serie
        self._brand = brand
        self._model = model
        self._amount = amount
    
    @property
    def serie(self):
        return self._serie
    
    @serie.setter
    def serie(self, value):
        self._serie = value

    @property
    def brand(self):
        return self._brand
    
    @brand.setter
    def brand(self, value):
        self._brand = value
    
    @property
    def model(self):
        return self._model
    
    @model.setter
    def model(self, value):
        self._model = value
    
    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def amount(self, value):
        self._amount = value

class VehicleManager:
    def __init__(self):
        self._vehicles = []
        self._idVehicle = 1
    
    def appendVehicle(self, serie, brand, model, amount):
        vehicle = Vehicle(serie, brand, model, amount)
        self._vehicles.append({"id": self._idVehicle, "vehicle": vehicle})
        self._idVehicle += 1
        print("Vehiculo agregado exitosamente!")
    
    def showVehicles(self):
        if not self._vehicles:
            print("No hoy vehículos registrados")
        else:
            for entry in self._vehicles:
                vehicle = entry["vehicle"]
                print(f"ID: {entry['id']}, Name: {vehicle.serie}, Serie: {vehicle.brand}, Brand: {vehicle.model}, Amount: {vehicle.amount}")
    
    def upVehicle(self, id, serie=None, brand=None, model=None, amount=None):
        for entry in self._vehicles:
            if entry["id"] == id:
                vehicle = entry["vehicle"]
                if serie is not None:
                    vehicle.serie = serie
                if brand is not None:
                    vehicle.brand = brand
                if model is not None:
                    vehicle.amount = amount
                print("Vehiculo modificado exitosamente!")
                return
        print("Vehiculo no encontrado")
    
    def deleteVehicle(self, id):
        for entry in self._vehicles:
            if entry["id"] == id:
                self._vehicles.remove(entry)
                print("Vehiculo eliminado con éxito!")
                return
        print("Vehiculo no encontrado")
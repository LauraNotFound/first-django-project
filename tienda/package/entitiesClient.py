class Client:
    def __init__(self, name, lastName, numberVehicles):
        self._name = name
        self._lastName = lastName
        self._numberVehicles = numberVehicles
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
    
    @property
    def lastName(self):
        return self._lastName
    
    @lastName.setter
    def lastName(self, value):
        self._lastName = value
    
    @property
    def numberVehicles(self):
        return self._numberVehicles
    
    @numberVehicles.setter
    def numberVehicles(self, value):
        self._numberVehicles = value

class ClientManager:
    def __init__(self):
        self._clients = []
        self._id_client = 1

    def appendClient(self, name, lastName, numberVehicles):
        client = Client(name, lastName, numberVehicles)
        self._clients.append({"id": self._id_client, "client": client})
        self._id_client += 1
        print("Cliente agregado exitosamente!")

    def showClients(self):
        if not self._clients:
            print("No hay clientes registrados")
        else:
            for entry in self._clients:
                client = entry["client"]
                print(f"ID: {entry['id']}, Name: {client.name}, Last Name: {client.lastName}, Number of Vehicles: {client.numberVehicles}")

    def upClient(self, id, name=None, lastName=None, numberVehicles=None):
        for entry in self._clients:
            if entry["id"] == id:
                client = entry["client"]
                if name is not None:
                    client.name = name
                if lastName is not None:
                    client.lastName = lastName
                if numberVehicles is not None:
                    client.numberVehicles = numberVehicles
                print("Cliente modificado exitosamente!")
                return
        print("Cliente no encontrado.")

    def deleteClient(self, id):
        for entry in self._clients:
            if entry["id"] == id:
                self._clients.remove(entry)
                print("Cliente eliminado exitosamente!")
                return
        print("Cliente no encontrado")
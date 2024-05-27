class Person:
    def __init__(self, dni, lastName, name, height, numVehicles):
        self.dni = dni
        self.lastName = lastName
        self.name = name
        self.height = height
        self.numVehicles = numVehicles

    def setDNI(self, dni):
        self.dni = dni
    
    def getDNI(self):
        return self.dni
    
    def setLastName(self, lastName):
        self.lastName = lastName
    
    def getLastName(self):
        return self.lastName
    
    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name

    def setHeight(self, height):
        self.height = height
    
    def getHeight(self):
        return self.height
    
    def setNumVehicles(self, numVehicles):
        self.numVehicles = numVehicles
    
    def getNumVehicles(self):
        return self.numVehicles
    
    def printData(self):
        print("DNI: ", self.getDNI())
        print("LastName: ", self.getLastName())
        print("Name: ", self.getName())
        print("Height: ", self.getHeight(), "m")
        print("Number of Vehicles: ", self.getNumVehicles(), "vehicles.")
        print()
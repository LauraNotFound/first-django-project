class Vehicle:
    def __init__(self, brand, model, color, speed, mileage):
        self.brand = brand
        self.model = model
        self.color = color
        self.speed = speed
        self.mileage = mileage

    def setBrand(self, brand):
        self.brand = brand
    
    def getBrand(self):
        return self.brand
    
    def setModel(self, model):
        self.model = model
    
    def getModel(self):
        return self.model

    def setColor(self, color):
        self.color = color
    
    def getColor(self):
        return self.color
    
    def setSpeed(self, speed):
        self.speed = speed
    
    def getSpeed(self):
        return self.speed
    
    def setMileage(self, mileage):
        self.mileage = mileage
    
    def getMileage(self):
        return self.mileage
    
    def speedVariation(self, variation):
        self.speed += variation
    
    def mileageVariation(self, variation):
        self.mileage += variation

    def printData(self):
        print("Brand: ", self.getBrand())
        print("Model: ", self.getModel())
        print("Color: ", self.getColor())
        print("Speed: ", self.getSpeed(), "km/h")
        print("Mileage: ", self.getMileage(), "km")
        print()
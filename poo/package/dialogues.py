from .entities import *
from .validations import *

def registerAVehicle():
    brand = read_text("Brand: ")
    model = read_text("Model: ")
    color = read_text("Color: ")
    speed = read_float("Speed: ")
    mileage = read_float("Mileage: ")
    myVehicle = Vehicle(brand, model, color, speed, mileage)
    myVehicle.printData()
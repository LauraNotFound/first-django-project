from .entities import *
from .validations import *

def registerAPerson():
    dni = read_text("DNI: ")
    lastName = read_text("LastName: ")
    name = read_text("Name: ")
    height = read_float("Height: ")
    numVehicles = read_int("Number of vehicles: ")
    person = Person(dni, lastName, name, height, numVehicles)
    person.printData()
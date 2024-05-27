#Script para detectar si el texto ingresado es un nombre, por lo cual no debe contener caracteres especiales.
import re
def is_name(name):
    txt = name.lower()
    regex = r'[*/¿)-_(&%$#|°@{};,.><0123456789\s]'
    chartetspecial = re.findall(regex, txt)
    return len(chartetspecial) == 0
    
texto = input("Ingrese el texto: ")
print("¿El texto es un nombre?", is_name(texto))
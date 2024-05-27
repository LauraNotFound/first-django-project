def read_text(text):
    entrada = ""
    while entrada == "":
        entrada = input(text)
    return entrada

def is_float(number_str):
    points = number_str.count('.')
    if points <= 1:
        if number_str.replace('.','').isdigit() == True:
            return True
        else:
            return False
    else:
        return False

def read_float(text):
    entrada = ""
    while is_float(entrada) != True:
        entrada = input(text)
    return float(entrada)
 
def is_int(number_str):
    if number_str.isdigit() == True:
        return True
    else:
        return False
    
def read_int(text):
    entrada = ""
    while is_int(entrada) != True:
        entrada = input(text)
    return int(entrada)

# import re

# def is_name(name):
#     txt = name.lower()
#     regex = r'[*/¿)-_(&%$#|°@{};,.><0123456789\s]'
#     chartetspecial = re.findall(regex, txt)
#     return len(chartetspecial) == 0

# def read_name(text):
#     entrada = ""
#     while is_name(entrada) != True:
#         entrada = input(text)
#     return entrada

# def is_dni(dni):
#     regex = r'[a-zA-Z*/¿)(&%$#|°@{};,.><\s]'
#     chartetspecial = re.findall(regex, dni)
#     tamanio=len(chartetspecial)
#     return tamanio == 0

# def read_dni(text):
#     entrada = ""
#     while is_dni(entrada) != True:
#         entrada = input(text)
#     return entrada
def is_int(number_str):
    if number_str.isdigit():
        return True
    else:
        return False

def read_int(text):
    entrada = ""
    while is_int(entrada) != True:
        entrada = input(text)
    return int(entrada)

def is_float(number_str):
    points = number_str.count('.')
    if points <= 1:
        if number_str.replace('.','').isdigit():
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

def read_text(text):
    entrada = ""
    while entrada == "":
        entrada = input(text)
    return entrada
import re
import os
import platform


def limpiar_pantalla():
    os.system('cls') if platform.system() == "Windows" else os.system('clear')


def leer_texto(longitud_min=0, longitud_max=100, mensaje=None):
    print(mensaje) if mensaje else None
    while True:
        texto = input("> ")
        if len(texto) >= longitud_min and len(texto) <= longitud_max:
            return texto


def bastidor_valido(bastidor, lista):
    if not re.match('[0-9]{2}[A-Z]$', bastidor):
        print("número de bastidor incorrecto, debe cumplir el formato.")
        return False
    for vehiculo in lista:
        if vehiculo.bastidor == bastidor:
            print("número de bastidor utilizado por otro vehículo.")
            return False
    return True

def ruedas_validas(ruedas):
    if not ruedas.isdigit():
        print("número de ruedas incorrecto, debe ser un número entero.")
        return False
    return True

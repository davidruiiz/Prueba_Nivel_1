import csv
import config

class Vehiculo:
    def __init__(self, color: str, ruedas: int):
        self.color = color
        self.ruedas = ruedas

#Creo un método que me muestre el color y el numero de ruedas del coche

    def __str__(self):
        return "color {}, {} ruedas".format( self.color, self.ruedas )
    

    def to_dict(self):
        return {
            "color": self.color,
            "ruedas": self.ruedas
        }
    
class Vehiculos:

    vehiculos = []
    with open(config.DATABASE_PATH, newline='\n') as fichero:
        reader = csv.reader(fichero, delimiter=';')
        for color, ruedas in reader:
            vehiculo = Vehiculo(color, ruedas)
            vehiculos.append(vehiculo)
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

    @staticmethod
    def buscar(dni):
        for vehiculo in Vehiculos.vehiculos:
            if vehiculo.dni == dni:
                return vehiculo
        return None
    
    @staticmethod
    def crear(color, ruedas):
        vehiculo = Vehiculo(color, ruedas)
        Vehiculos.vehiculos.append(vehiculo)
        Vehiculos.guardar()
        return vehiculo
    
    @staticmethod
    def modificar(color, ruedas):
        for indice, vehiculo in enumerate(Vehiculos.vehiculos):
            if vehiculo.color == color:
                Vehiculos.vehiculos[indice].ruedas = ruedas
                Vehiculos.guardar() 
                return vehiculo
            
    @staticmethod
    def borrar(color):
        for indice, vehiculo in enumerate(Vehiculos.vehiculos):
            if vehiculo.color == color:
                del Vehiculos.vehiculos[indice]
                Vehiculos.guardar()
                return vehiculo
            
    @staticmethod
    def guardar():
        with open(config.DATABASE_PATH, 'w', newline='\n') as fichero:
            writer = csv.writer(fichero, delimiter=';')
            for vehiculo in Vehiculos.vehiculos:
                writer.writerow([vehiculo.color, vehiculo.ruedas])


#Creo una clase Vehiculo con el constructor de la clase y los atributos color y ruedas

class Vehiculo():

    def __init__(self, color: str, ruedas: int):
        self.color = color
        self.ruedas = ruedas

#Creo un método que me muestre el color y el numero de ruedas del coche

    def __str__(self):
        return "color {}, {} ruedas".format( self.color, self.ruedas )
    

from vehiculo import Vehiculo

#Creo una clase Coche que hereda de la clase Vehiculo y que tiene como atributos velocidad y cilindrada

class Coche(Vehiculo):

    def __init__(self, color: str, ruedas: int, velocidad: int, cilindrada: int):
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    #Creo un método que me muestre el color y el numero de ruedas del coche, su velocidad y su cilindrada

    def __str__(self):
        return Vehiculo.__str__(self) + ", {} km/h, {} cc".format( self.velocidad, self.cilindrada )
    
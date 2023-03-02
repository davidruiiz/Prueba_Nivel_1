# Importamos la clase Bicicleta del fichero bicicleta.py
from bicicleta import Bicicleta

# Definimos la clase Motocicleta como una subclase de Bicicleta
class Motocicleta(Bicicleta):
    # Definimos el constructor de la clase Motocicleta
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        # Invocamos el constructor de la superclase Bicicleta
        Bicicleta.__init__(self, color, ruedas, tipo)
        # Definimos los atributos de la clase Motocicleta
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    # Definimos el método especial __str__
    def __str__(self):
        # Invocamos el método especial __str__ de la superclase Bicicleta
        return Bicicleta.__str__(self) + ", {} km/h, {} cc".format( self.velocidad, self.cilindrada )
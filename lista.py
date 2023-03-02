# Crea al menos un objeto de cada subclase y añádelos a una lista llamada vehiculos.

from coche import Coche
from bicicleta import Bicicleta
from camioneta import Camioneta
from motocicleta import Motocicleta

# Create a list of vehicles
vehiculos = []

# Create a car object
coche = Coche("rojo", 4, 180, 1600)
# Add the car object to the list
vehiculos.append(coche)

# Create a bicycle object
bicicleta = Bicicleta("azul", 2, "urbana")
# Add the bicycle object to the list
vehiculos.append(bicicleta)

# Create a truck object
camioneta = Camioneta("blanco", 4, 120, 2000, 500)
# Add the truck object to the list
vehiculos.append(camioneta)

# Create a motorcycle object
motocicleta =  
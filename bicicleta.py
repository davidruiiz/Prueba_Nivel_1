from  vehiculo import Vehiculo

# Esta clase hereda de la clase Vehiculo
class Bicicleta(Vehiculo):
    
        # El constructor de la clase Bicicleta recibe los parámetros del constructor
        # de la clase padre Vehiculo, y los parámetros propios de la clase Bicicleta
        def __init__(self, color: str, ruedas: int, tipo: str):
            # Se invoca al constructor de la clase padre Vehiculo
            Vehiculo.__init__(self, color, ruedas)
            # Se inicializa el atributo propio de la clase Bicicleta
            self.tipo = tipo
    
        # Se redefine el método __str__ de la clase padre Vehiculo
        def __str__(self):
            # Se invoca al método __str__ de la clase padre Vehiculo
            return Vehiculo.__str__(self) + ", {}".format( self.tipo )


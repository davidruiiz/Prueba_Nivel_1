from coche import Coche

# Define a class named Camioneta that inherits from Coche
class Camioneta(Coche):
    # Define the constructor of the class
    def __init__(self, color: str, ruedas: int, velocidad: int, cilindrada: int, carga: int):
        # Call the constructor of the parent class with the super() function
        super().__init__(color, ruedas, velocidad, cilindrada)
        # Set the value of the attribute carga
        self.carga = carga
    # Define the __str__ method
    def __str__(self):
        # Call the __str__ method of the parent class with the super() function
        return super().__str__() + ", {} kg de carga".format( self.carga )
    

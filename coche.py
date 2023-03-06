from database import Vehiculo

#Creo una clase Coche que hereda de la clase Vehiculo y que tiene como atributos velocidad y cilindrada

class Coche(Vehiculo):
    def __init__(self, bastidor: str, color: str, ruedas: int, velocidad: int, cilindrada: int) -> None:
        # Llamamos a la clase padre (Vehiculo) para que ejecute su constructor
        super().__init__(bastidor, color, ruedas)
        # Creamos nuestro atributo propio
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self) -> str:
        # Llamamos a la clase padre para que nos devuelva su representación en formato string
        return f"Coche: {self.bastidor}, {self.color}, {self.ruedas}, {self.velocidad}, {self.cilindrada}"

    def to_dict(self):
        # Llamamos a la clase padre para que nos devuelva su representación en forma de diccionario
        return {
            "bastidor": self.bastidor,
            "color": self.color,
            "ruedas": self.ruedas,
            "velocidad": self.velocidad,
            "cilindrada": self.cilindrada
        }
    

  
    
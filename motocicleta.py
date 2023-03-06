from bicicleta import Bicicleta

# Creo una clase Motocicleta que hereda de la clase Bicicleta y que tiene como atributos velocidad y cilindrada

class Motocicleta(Bicicleta):
    def __init__(self, bastidor: str, color: str, ruedas: int, tipo: str, velocidad: int, cilindrada: int) -> None:
        # Llamamos a la clase padre (Bicicleta) para que ejecute su constructor
        super().__init__(bastidor, color, ruedas, tipo)
        # Creamos nuestro atributo propio
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self) -> str:
        # Llamamos a la clase padre para que nos devuelva su representación en formato string
        return f"Motocicleta: {self.bastidor}, {self.color}, {self.ruedas}, {self.tipo}, {self.velocidad}, {self.cilindrada}"

    def to_dict(self):
        # Llamamos a la clase padre para que nos devuelva su representación en forma de diccionario
        return {
            "bastidor": self.bastidor,
            "color": self.color,
            "ruedas": self.ruedas,
            "tipo": self.tipo,
            "velocidad": self.velocidad,
            "cilindrada": self.cilindrada
        }


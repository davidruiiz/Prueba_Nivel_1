from coche import Coche

#Creo una clase Camioneta que hereda de la clase Coche y que tiene como atributo carga

class Camioneta(Coche):
    def __init__(self, bastidor: str, color: str, ruedas: int, velocidad: int, cilindrada: int, carga: int) -> None:
        # Llamamos a la clase padre (Coche) para que ejecute su constructor
        super().__init__(bastidor, color, ruedas, velocidad, cilindrada)
        # Creamos nuestro atributo propio
        self.carga = carga

    def __str__(self) -> str:
        # Llamamos a la clase padre para que nos devuelva su representación en formato string
        return f"Camioneta: {self.bastidor}, {self.color}, {self.ruedas}, {self.velocidad}, {self.cilindrada}, {self.carga}"

    def to_dict(self):
        # Llamamos a la clase padre para que nos devuelva su representación en forma de diccionario
        return {
            "bastidor": self.bastidor,
            "color": self.color,
            "ruedas": self.ruedas,
            "velocidad": self.velocidad,
            "cilindrada": self.cilindrada,
            "carga": self.carga
        }
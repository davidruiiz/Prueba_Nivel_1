from  database import Vehiculo

# Creo una clase Bicicleta que hereda de la clase Vehiculo y que tiene como atributo tipo (urbana o montaña)

class  Bicicleta ( Vehiculo ):
        def   __init__ ( self , bastidor: str , color: str , ruedas: int , tipo: str ) -> None :
            # Llamamos a la clase padre (Vehiculo) para que ejecute su constructor
            super () . __init__ ( bastidor , color , ruedas )
            # Creamos nuestro atributo propio
            self.tipo  =  tipo
    
        def   __str__ ( self ):
            # Llamamos a la clase padre para que nos devuelva su representación en formato string
            return f"Bicicleta: { self.bastidor } , { self.color } , { self.ruedas } , { self.tipo }"
    
        def  to_dict ( self ):
            # Llamamos a la clase padre para que nos devuelva su representación en forma de diccionario
            return {
                "bastidor" :  self.bastidor ,
                "color" :  self.color ,
                "ruedas" :  self.ruedas ,
                "tipo" :  self.tipo 
            }

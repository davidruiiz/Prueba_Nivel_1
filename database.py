import csv
import config


class Vehiculo:
    def __init__(self, bastidor, color, ruedas):
        self.bastidor = bastidor
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f"({self.bastidor}) {self.color} {self.ruedas}"

    def to_dict(self):
        return {'bastidor': self.bastidor, 'color': self.color, 'ruedas': self.ruedas}


class Vehiculos:

    lista = []
    with open(config.DATABASE_PATH, newline='\n') as fichero:
        reader = csv.reader(fichero, delimiter=';')
        for bastidor, color, ruedas in reader:
            vehiculo = Vehiculo(bastidor, color, ruedas)
            lista.append(vehiculo)

    @staticmethod
    def buscar(bastidor):
        for vehiculo in Vehiculos.lista:
            if vehiculo.bastidor == bastidor:
                return vehiculo

    @staticmethod
    def crear(bastidor, color, ruedas):
        vehiculo = Vehiculo(bastidor, color, ruedas)
        Vehiculos.lista.append(vehiculo)
        Vehiculos.guardar()
        return vehiculo

    @staticmethod
    def modificar(bastidor, color, ruedas):
        for indice, vehiculo in enumerate(Vehiculos.lista):
            if vehiculo.bastidor == bastidor:
                Vehiculos.lista[indice].color = color
                Vehiculos.lista[indice].ruedas = ruedas
                Vehiculos.guardar()
                return Vehiculos.lista[indice]

    @staticmethod
    def borrar(bastidor):
        for indice, vehiculo in enumerate(Vehiculos.lista):
            if vehiculo.bastidor == bastidor:
                vehiculo = Vehiculos.lista.pop(indice)
                Vehiculos.guardar()
                return vehiculo

    @staticmethod
    def guardar():
        with open(config.DATABASE_PATH, 'w', newline='\n') as fichero:
            writer = csv.writer(fichero, delimiter=';')
            for vehiculo in Vehiculos.lista:
                writer.writerow((vehiculo.bastidor, vehiculo.color, vehiculo.ruedas))
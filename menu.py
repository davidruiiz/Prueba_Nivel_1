import os
import helpers
import database as db


def iniciar():
    while True:
        helpers.limpiar_pantalla()

        print("=========================")
        print("  Bienvenido al Gestor   ")
        print("=========================")
        print("[1] Listar los vehículos ")
        print("[2] Buscar un vehículo   ")
        print("[3] Añadir un vehículo   ")
        print("[4] Modificar un vehículo")
        print("[5] Borrar un vehículo   ") 
        print("[6] Cerrar el Gestor     ")
        print("=========================")

        opcion = input("> ")
        helpers.limpiar_pantalla()

        if opcion == '1':
            print("Listando los vehículos...\n")
            for vehiculo in db.Vehiculos.lista:
                print(vehiculo)

        elif opcion == '2':
            print("Buscando un vehiculo...\n")
            bastidor = helpers.leer_texto(3, 3, "Número de Bastidor").upper()
            vehiculo = db.Vehiculos.buscar(bastidor)
            print(vehiculo) if vehiculo else print("Vehículo no encontrado.")

        elif opcion == '3':
            print("Añadiendo un vehículo...\n")

            bastidor = None
            while True:
                bastidor = helpers.leer_texto(3, 3, "Número de Bastidor").upper()
                if helpers.bastidor_valido(bastidor, db.Vehiculos.lista):
                    break

            color = helpers.leer_texto(2, 30, "Color").capitalize()
            ruedas = helpers.leer_texto(2, 30, "Número de ruedas").capitalize()
            db.Vehiculos.crear(bastidor, color, ruedas)
            print("Vehículo añadido correctamente.")

        elif opcion == '4':
            print("Modificando un vehículo...\n")
            bastidor = helpers.leer_texto(3, 3, "Número de bastidor").upper()
            vehiculo = db.Vehiculos.buscar(bastidor)
            if vehiculo:
                color = helpers.leer_texto(
                    2, 30, f"Color [{vehiculo.color}]").capitalize()
                ruedas = helpers.leer_texto(
                    2, 30, f"Número de ruedas [{vehiculo.apellido}]").capitalize()
                db.Vehiculos.modificar(vehiculo.bastidor, color, ruedas)
                print("Vehículo modificado correctamente.")
            else:
                print("Vehículo no encontrado.")

        elif opcion == '5':
            print("Borrando un vehículo...\n")
            bastidor = helpers.leer_texto(3, 3, "Número de Bastidor").upper()
            print("Vehiculo borrado correctamente.") if db.Vehiculos.borrar(
                bastidor) else print("Vehículo no encontrado.")

        elif opcion == '6':
            print("Saliendo...\n")
            break

        input("\nPresiona ENTER para continuar...")

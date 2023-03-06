from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, constr, validator
import database as db
import helpers


headers = {"content-type": "charset=utf-8"}


class ModeloVehiculo(BaseModel):
    color: constr(min_length=3, max_length=3)
    ruedas: constr(min_length=2, max_length=30)
    


class ModeloCrearVehiculo(ModeloVehiculo):
    @validator("color")
    def validar_dni(cls, color):
        if not helpers.dni_valido(color, db.Vehiculos.lista):
            raise ValueError("Vehículo ya existente o número de bastidor incorrecto")
        return color


app = FastAPI(
    title="API del Gestor de vehículos",
    description="Ofrece diferentes funciones para gestionar los vehículos.")


@app.get("/vehículos/", tags=["Vehículos"])
async def vehiculos():
    content = [vehiculo.to_dict() for vehiculo in db.Vehiculos.lista]
    return JSONResponse(content=content, headers=headers)


@app.get("/vehiculos/buscar/{color}/", tags=["Vehiculos"])
async def vehiculos_buscar(color: str):
    vehiculo = db.Vehiculos.buscar(color=color)
    if not vehiculo:
        raise HTTPException(status_code=404, detail="Vehiculo no encontrado")
    return JSONResponse(content=vehiculo.to_dict(), headers=headers)


@app.post("/vehiculos/crear/", tags=["Vehiculos"])
async def vehiculos_crear(datos: ModeloCrearVehiculo):
    vehiculo = db.Vehiculos.crear(datos.color, datos.ruedas)
    if vehiculo:
        return JSONResponse(content=vehiculo.to_dict(), headers=headers)
    raise HTTPException(status_code=404)


@ app.put("/vehiculos/actualizar/", tags=["Clientes"])
async def clientes_actualizar(datos: ModeloVehiculo):
    if db.Vehiculos.buscar(datos.color):
        vehiculo = db.Vehiculos.modificar(datos.color, datos.ruedas)
        if vehiculo:
            return JSONResponse(content=vehiculo.to_dict(), headers=headers)
    raise HTTPException(status_code=404)


@app.delete("/vehiculos/borrar/{color}/", tags=["Clientes"])
async def vehiculos_borrar(color: str):
    if db.Vehiculos.buscar(color=color):
        vehiculo = db.Vehiculos.borrar(color=color)
        return JSONResponse(content=vehiculo.to_dict(), headers=headers)
    raise HTTPException(status_code=404)

print("Servidor de la API...")
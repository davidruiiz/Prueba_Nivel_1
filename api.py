from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, constr, validator
import database as db
import helpers


headers = {"content-type": "charset=utf-8"}


class ModeloVehiculo(BaseModel):
    bastidor: constr(min_length=3, max_length=3)
    color: constr(min_length=2, max_length=30)
    ruedas: constr(min_length=2, max_length=30)


class ModeloCrearVehiculo(ModeloVehiculo):
    @validator("bastidor")
    def validar_bastidor(cls, bastidor):
        if not helpers.bastidor_valido(bastidor, db.Vehiculos.lista):
            raise ValueError("Vehículo ya existente o DNI incorrecto")
        return bastidor


app = FastAPI(
    title="API del Gestor de vehículos",
    description="Ofrece diferentes funciones para gestionar los vehículos.")


@app.get("/vehículos/", tags=["Vehículos"])
async def vehiculos():
    content = [vehiculo.to_dict() for vehiculo in db.Vehiculos.lista]
    return JSONResponse(content=content, headers=headers)


@app.get("/vehiculos/buscar/{bastidor}/", tags=["Vehículos"])
async def vehiculos_buscar(bastidor: str):
    vehiculo = db.Vehiculos.buscar(bastidor=bastidor)
    if not vehiculo:
        raise HTTPException(status_code=404, detail="Vehículo no encontrado")
    return JSONResponse(content=vehiculo.to_dict(), headers=headers)


@app.post("/vehiculos/crear/", tags=["Vehículos"])
async def vehiculos_crear(datos: ModeloCrearVehiculo):
    vehiculo = db.Vehiculos.crear(datos.bastidor, datos.color, datos.ruedas)
    if vehiculo:
        return JSONResponse(content=vehiculo.to_dict(), headers=headers)
    raise HTTPException(status_code=404)


@ app.put("/vehiculos/actualizar/", tags=["Vehículos"])
async def vehiculos_actualizar(datos: ModeloVehiculo):
    if db.Vehiculos.buscar(datos.bastidor):
        vehiculo = db.Vehiculos.modificar(datos.bastidor, datos.color, datos.ruedas)
        if vehiculo:
            return JSONResponse(content=vehiculo.to_dict(), headers=headers)
    raise HTTPException(status_code=404)


@app.delete("/vehiculos/borrar/{bastidor}/", tags=["Vehículos"])
async def vehiculos_borrar(bastidor: str):
    if db.Vehiculos.buscar(bastidor=bastidor):
        vehiculo = db.Vehiculos.borrar(bastidor=bastidor)
        return JSONResponse(content=vehiculo.to_dict(), headers=headers)
    raise HTTPException(status_code=404)

print("Servidor de la API...")

from fastapi import APIRouter, HTTPException, Path, Depends
from app.config import Sessionlocal
from sqlalchemy.orm import Session
from app.schemas import compraSchema, requestCompra,responseCompra
from app.controllers.compra_controller import CompraController
from app.services.compra_service import CompraService
from datetime import date

compra_router = APIRouter(prefix="/compra")

compra_controller = CompraController(service=CompraService)

def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        pass
    db.close()


@compra_router.get("/listAll")
async def get_compras():
    return compra_controller.getCompras(Sessionlocal())

@compra_router.get("/listById")
async def get_compra_by_codigo(id_compra : int):
    return compra_controller.getCompra_byId(Sessionlocal(), id_compra)

@compra_router.get("/listByData")
async def get_compra_by_codigo(data : date):
    return compra_controller.getCompras_byData(Sessionlocal(), data)

@compra_router.post("/create")
async def criar_compra(compra : requestCompra):
    return 200 if compra_controller.createCompra(Sessionlocal(), compra) else 400

@compra_router.delete("/delete")
async def delete_compra(id_compra: int):
    return 200 if compra_controller.remove_compra(Sessionlocal(), id_compra) else 400




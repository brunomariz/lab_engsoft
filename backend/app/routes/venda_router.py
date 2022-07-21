from fastapi import APIRouter, HTTPException, Path, Depends
from app.config import Sessionlocal
from sqlalchemy.orm import Session
from app.schemas import vendaSchema, requestVenda, responseVenda
from app.controllers.venda_controller import vendaController
from app.services.venda_service import vendaService

venda_router = APIRouter(prefix="/venda")

venda_controller = vendaController(service=vendaService)

def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        pass
    db.close()

@venda_router.get("/")
async def get_vendas():
    return venda_controller.getVendas(Sessionlocal())

@venda_router.get("/venda")
async def search_venda(request:requestVenda):
    return venda_controller.get_vendaEspecifico(Sessionlocal(),request)

@venda_router.post("/create")
async def create_venda(request:requestVenda):
    return venda_controller.create_venda(Sessionlocal(), request)

@venda_router.post("/remove")
async def remove_venda(request:requestVenda):
    return venda_controller.remove_venda(Sessionlocal(), request)

@venda_router.post("/update")
async def update_venda(request:requestVenda):
    return venda_controller.update_venda(Sessionlocal(), request)
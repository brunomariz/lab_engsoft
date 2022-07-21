from fastapi import APIRouter, HTTPException, Path, Depends
from app.config import Sessionlocal
from sqlalchemy.orm import Session
from app.schemas import fornecedorSchema, requestFornecedor, responseFornecedor
from app.controllers.fornecedor_controller import fornecedorController
from app.fornecedor_service import fornecedorService


fornecedor_router = APIRouter(prefix="/fornecedor")

fornecedor_controller = fornecedorController(service=fornecedorService)

def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        pass
    db.close()

@fornecedor_router.get("/")
async def get_fornecedores():
    return fornecedor_controller.get_fornecedores(Sessionlocal())

@fornecedor_router.get("/fornecedor")
async def search_fornecedor(request:requestFornecedor, db:Session):
    return fornecedor_controller.get_fornecedorEspecifico(Sessionlocal(),request)

@fornecedor_router.post("/create")
async def create_fornecedor(request:requestFornecedor, db:Session):
    return fornecedor_controller.create_fornecedor(Sessionlocal(), request)

@fornecedor_router.post("/remove")
async def create_fornecedor(request:requestFornecedor, db:Session):
    return fornecedor_controller.remove_fornecedor(Sessionlocal(), request)

@fornecedor_router.post("/update")
async def update_fornecedor(request:requestFornecedor, db:Session):
    return fornecedor_controller.update_fornecedor(Sessionlocal(), request)

# @fornecedor_router.post("/create")
# async def create_fornecedore(request:requestfornecedore, db:Sessionget_db)):
#     return fornecedor_controller.create_fornecedore(db, request)

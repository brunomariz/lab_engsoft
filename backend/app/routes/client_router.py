from fastapi import APIRouter, HTTPException, Path, Depends
from app.config import Sessionlocal
from sqlalchemy.orm import Session
from app.schemas import clienteSchema, requestCliente, responseCliente
from app.controllers.client_controller import ClientController
from app.clienteCRUD import ClientService


client_router = APIRouter(prefix="/client")

client_controller = ClientController(service=ClientService)

def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        pass
    db.close()

@client_router.get("/")
async def get_clientes():
    return client_controller.get_clientes(Sessionlocal())

@client_router.get("/cliente")
async def search_clientes(request:requestCliente, db:Session):
    return client_controller.get_clienteEspecifico(request)

@client_router.post("/create")
async def create_cliente(request:requestCliente, db:Session):
    return client_controller.create_cliente(db, request)

@client_router.post("/remove")
async def create_cliente(request:requestCliente, db:Session):
    return client_controller.remove_cliente(db, request)

@client_router.post("/update")
async def update_cliente(request:requestCliente, db:Session):
    return client_controller.update_cliente(db, request)

# @client_router.post("/create")
# async def create_cliente(request:requestCliente, db:Sessionget_db)):
#     return client_controller.create_cliente(db, request)

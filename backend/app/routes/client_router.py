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

@client_router.post("/cliente")
async def search_clientes(request:requestCliente): #request:requestCliente
    return client_controller.get_clientes(Sessionlocal())
    #return client_controller.get_clienteEspecifico(Sessionlocal(), request)

# @client_router.post("/create")
# async def create_cliente(request:requestCliente, db:Session):
#     return client_controller.create_cliente(Sessionlocal(), request)

# @client_router.post("/remove")
# async def remove_cliente(request:requestCliente, db:Session):
#     return client_controller.remove_cliente(Sessionlocal(), request)

# @client_router.post("/update")
# async def update_cliente(request:requestCliente, db:Session):
#     return client_controller.update_cliente(Sessionlocal(), request)

# @client_router.post("/create")
# async def create_cliente(request:requestCliente, db:Session=Depends(get_db)):
#     return client_controller.create_cliente(db, request)

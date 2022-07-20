from fastapi import APIRouter, HTTPException, Path, Depends
from app.config import Sessionlocal
from sqlalchemy.orm import Session
from app.schemas import clienteSchema, requestCliente, responseCliente
from app.controllers.client_controller import ClientController
from app.clienteCRUD import clientCRUD


client_router = APIRouter(prefix="/client")

client_controller = ClientController(service=clienteCRUD)

def get_db():
    db = Sessionlocal
    try:
        yield db
    finally:
        db.close()

@client_router.get("/")
async def get_clientes():
    return client_controller.get_clientes()


@client_router.post("/create")
async def get_client_additional_method(request:requestCliente, db:Session=Depends(get_db)):
    client_controller.create_cliente(db, request)
    
    return responseCliente(code=200, status='ok', message="Cliente criado com sucesso")

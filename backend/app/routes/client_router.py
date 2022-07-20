from fastapi.routing import APIRouter
from app.controllers.client_controller import ClientController


client_router = APIRouter(prefix="/client")

client_controller = ClientController()


@client_router.get("/")
async def get_clientes():
    return client_controller.get_clientes()


@client_router.get("/additional_method")
async def get_client_additional_method():
    return client_controller.client_additional_method()

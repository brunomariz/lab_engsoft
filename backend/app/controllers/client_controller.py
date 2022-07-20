from app.controllers._base import BaseController
from app.services.cliente_service import ClientService
from sqlalchemy.orm import Session
from app.schemas import clienteSchema, requestCliente, responseCliente
import app.clienteCRUD

class ClientController(BaseController):
    def __init__(self, service=...) -> None:
        super().__init__(ClientService())

    def get_clientes(self):
        return self.service.list_clientes()
    def create_cliente(self,db:Session, requestCliente):
        return self.service.create_cliente(db, requestCliente.parameter)

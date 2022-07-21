from app.controllers._base import BaseController
from sqlalchemy.orm import Session
from app.schemas import clienteSchema, requestCliente, responseCliente
from app.clienteCRUD import ClientService

class ClientController(BaseController):
    def __init__(self, service=...) -> None:
        super().__init__(ClientService())

    def get_clientes(self,db:Session):
        return self.service.getClientes(db=db)
    def create_cliente(self,db:Session, requestCliente):
        return self.service.create_cliente(db, requestCliente.parameter)
    def create_cliente(self,db:Session, requestCliente):
        return self.service.create_cliente(db, requestCliente.parameter)
    def create_cliente(self,db:Session, requestCliente):
        return self.service.create_cliente(db, requestCliente.parameter)
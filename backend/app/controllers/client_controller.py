from app.controllers._base import BaseController
from app.services.cliente_service import ClientService
from sqlalchemy.orm import Session
from schemas import clienteSchema, requestCliente, responseCliente
import clienteCRUD

# Session.query

class ClientController(BaseController):
    def __init__(self, service=...) -> None:
        super().__init__(ClientService())

    def getClientes(self,db:Session, requestCliente):
        return self.service.get_Clientes(db)
    def get_clienteEspecifico(self,db:Session, requestCliente):
        return self.service.get_ClienteEspecifico(db, requestCliente.parameter.CPF_cliente)
    def create_cliente(self,db:Session, requestCliente):
        return self.service.create_cliente(db, requestCliente.parameter)
    def remove_cliente(self,db:Session, requestCliente):
        return self.service.remove_cliente(db, requestCliente.parameter.CPF_cliente)
    def update_cliente(self,db:Session, requestCliente):
        return self.service.update_cliente(db, requestCliente.parameter.CPF_cliente, requestCliente.parameter.CPF_cliente)
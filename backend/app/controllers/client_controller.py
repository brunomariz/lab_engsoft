from app.controllers._base import BaseController
from sqlalchemy.orm import Session
from app.schemas import clienteSchema, requestCliente, responseCliente
from app.clienteCRUD import ClientService
import json

# Session.query

class ClientController(BaseController):
    def __init__(self, service=...) -> None:
        super().__init__(ClientService())

    def get_clientes(self,db:Session):
        return json.dumps([obj.toDict() for obj in self.service.getClientes(db)])

    def get_clienteEspecifico(self,db:Session, requestCliente):
        return json.dumps((self.service.getClienteEspecifico(db, requestCliente.CPF_cliente)).toDict())
        
    def create_cliente(self,db:Session, requestCliente):
        if self.service.createCliente(db, requestCliente):
            return responseCliente("200", "Ok", "Conta criada com sucesso")
        return responseCliente("400", "Erro", "Erro na criação da conta")

    def remove_cliente(self,db:Session, requestCliente):
        if self.service.removeCliente(db, requestCliente.CPF_cliente):
            return responseCliente("200", "Ok", "Conta excluída com sucesso")
        return responseCliente("400", "Erro", "Erro na exclusão da conta")

    def update_cliente(self,db:Session, requestCliente):
        if self.service.updateCliente(db, requestCliente.CPF_cliente, requestCliente.nome_cliente):
            return responseCliente("200", "Ok", "Conta atualizada com sucesso")
        return responseCliente("400", "Erro", "Erro na atualização da conta")
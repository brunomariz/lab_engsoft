from app.controllers._base import BaseController
from sqlalchemy.orm import Session
from app.schemas import fornecedorSchema, requestFornecedor, responseFornecedor
from app.services.fornecedor_service import fornecedorService
import json
# Session.query

class fornecedorController(BaseController):
    def __init__(self, service=...) -> None:
        super().__init__(fornecedorService())

    def get_fornecedores(self,db:Session):
        return json.dumps([obj.toDict() for obj in self.service.getFornecedores(db)])

    def get_fornecedorEspecifico(self,db:Session, request:requestFornecedor):
        return json.dumps([self.service.getFornecedorEspecifico(db, request.CPF_fornecedor).toDict()])

    def create_fornecedor(self,db:Session, request:requestFornecedor):
        return json.dumps([self.service.createFornecedor(db, request)])

    def remove_fornecedor(self,db:Session, request:requestFornecedor):
        return json.dumps([self.service.removeFornecedor(db, request.CPF_fornecedor)])

    def update_fornecedor(self,db:Session, request:requestFornecedor):
        return json.dumps([self.service.updateFornecedor(db, request.CPF_fornecedor, request.nome_fornecedor)])

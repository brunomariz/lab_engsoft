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
        return json.dumps([(self.service.getFornecedorEspecifico(db, request.CNPJ_fornecedor)).toDict()])

    def create_fornecedor(self,db:Session, request:requestFornecedor):
        if self.service.createFornecedor(db, request):
            return responseFornecedor("200","Ok","Fornecedor criado com sucesso")
        return responseFornecedor("400","Erro","Erro na criacao de fornecedor")

    def remove_fornecedor(self,db:Session, request:requestFornecedor):
        if self.service.removeFornecedor(db, request.CNPJ_fornecedor):
            return responseFornecedor("200","Ok","Fornecedor removido com sucesso")
        return responseFornecedor("400","Erro","Erro na remocao de fornecedor")

    def update_fornecedor(self,db:Session, request:requestFornecedor):
        if self.service.updateFornecedor(db, request.CNPJ_fornecedor, request.nome_fornecedor):
            return responseFornecedor("200","Ok","Fornecedor atualizado com sucesso")
        return responseFornecedor("400","Erro","Erro na atualizacao de fornecedor")

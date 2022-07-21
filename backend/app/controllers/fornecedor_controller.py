from app.controllers._base import BaseController
from sqlalchemy.orm import Session
from app.schemas import fornecedorSchema, requestFornecedor, responseFornecedor
from app.services.fornecedor_service import fornecedorService

# Session.query

class fornecedorController(BaseController):
    def __init__(self, service=...) -> None:
        super().__init__(fornecedorService())

    def get_fornecedores(self,db:Session):
        return self.service.getFornecedores(db)
    # def get_fornecedorEspecifico(self,db:Session, requestfornecedor):
    #     return self.service.getfornecedorEspecifico(db, requestfornecedor.parameter.CPF_fornecedor)
    # def create_fornecedor(self,db:Session, requestfornecedor):
    #     return self.service.createfornecedor(db, requestfornecedor.parameter)
    # def remove_fornecedor(self,db:Session, requestfornecedor):
    #     return self.service.removefornecedor(db, requestfornecedor.parameter.CPF_fornecedor)
    # def update_fornecedor(self,db:Session, requestfornecedor):
    #     return self.service.updatefornecedor(db, requestfornecedor.parameter.CPF_fornecedor, requestfornecedor.parameter.CPF_fornecedor)

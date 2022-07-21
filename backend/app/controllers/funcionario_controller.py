from app.controllers._base import BaseController
from sqlalchemy.orm import Session
from app.schemas import funcionarioSchema, requestFuncionario, responseFuncionario
from app.services.funcionario_service import funcionarioService
import json
# Session.query

class funcionarioController(BaseController):
    def __init__(self, service=...) -> None:
        super().__init__(funcionarioService())

    def get_funcionarios(self,db:Session):
        return json.dumps([obj.toDict() for obj in self.service.getFuncionarios(db)])

    def get_funcionarioEspecifico(self,db:Session, request: requestFuncionario):
        return json.dumps([self.service.getfuncionarioEspecifico(db, request.CPF_funcionario).toDict()])

    def create_funcionario(self,db:Session, request:requestFuncionario):
        return json.dumps([self.service.createfuncionario(db, request)])

    def remove_funcionario(self,db:Session, request:requestFuncionario):
        return json.dumps([self.service.removefuncionario(db, request.CPF_funcionario)])

    def update_funcionario(self,db:Session, request:requestFuncionario):
        return json.dumps([self.service.updatefuncionario(db, request.CPF_funcionario, request.nome_funcionario)])

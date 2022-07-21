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
        return json.dumps([(self.service.getfuncionarioEspecifico(db, request.CPF_funcionario)).toDict()])

    def create_funcionario(self,db:Session, request:requestFuncionario):
        if self.service.createfuncionario(db, request):
            return responseFuncionario("200","Ok","Funcionario criado com sucesso")
        return responseFuncionario("400","Erro","Erro na criacao de funcionario")

    def remove_funcionario(self,db:Session, request:requestFuncionario):
        if self.service.removefuncionario(db, request.CPF_funcionario):
            return responseFuncionario("200","Ok","Funcionario removido com sucesso")
        return responseFuncionario("400","Erro","Erro na remocao de funcionario")

    def update_funcionario(self,db:Session, request:requestFuncionario):
        if self.service.updatefuncionario(db, request.CPF_funcionario, request.nome_funcionario):
            return responseFuncionario("200","Ok","Funcionario atualizado com sucesso")
        return responseFuncionario("400","Erro","Erro na atualizacao de funcionario")

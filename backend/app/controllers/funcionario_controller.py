from app.controllers._base import BaseController
from sqlalchemy.orm import Session
from app.schemas import funcionarioSchema, requestFuncionario, responseFuncionario
from app.services.funcionario_service import funcionarioService
# Session.query

class funcionarioController(BaseController):
    def __init__(self, service=...) -> None:
        super().__init__(funcionarioService())

    def get_funcionarios(self,db:Session):
        return [obj.toDict() for obj in self.service.getFuncionarios(db)]

    def get_funcionarioEspecifico(self,db:Session, request: requestFuncionario):
        return [(self.service.getFuncionarioEspecifico(db, request.CPF_funcionario)).toDict()]

    def create_funcionario(self,db:Session, request:requestFuncionario):
        if self.service.createFuncionario(db, request):
            return responseFuncionario("200","Ok","Funcionario criado com sucesso")
        return responseFuncionario("400","Erro","Erro na criacao de funcionario")

    def remove_funcionario(self,db:Session, request:requestFuncionario):
        if self.service.removeFuncionario(db, request.CPF_funcionario):
            return responseFuncionario("200","Ok","Funcionario removido com sucesso")
        return responseFuncionario("400","Erro","Erro na remocao de funcionario")

    def update_funcionario(self,db:Session, request:requestFuncionario):
        if self.service.updateFuncionario(db, request.CPF_funcionario, request.nome_funcionario,request.salario_fixo,request.eh_gerente,request.comissao_venda, request.login_usuario):
            return responseFuncionario("200","Ok","Funcionario atualizado com sucesso")
        return responseFuncionario("400","Erro","Erro na atualizacao de funcionario")

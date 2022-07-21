from app.controllers._base import BaseController
from sqlalchemy.orm import Session
from app.schemas import salarioSchema, requestSalario, responseSalario
from app.services.salario_service import salarioService
import json
# Session.query

class salarioController(BaseController):
    def __init__(self, service=...) -> None:
        super().__init__(salarioService())

    def get_salarios(self,db:Session):
        return json.dumps([obj.toDict() for obj in self.service.getSalarios(db)])

    def get_salarioEspecifico(self,db:Session, request: requestSalario):
        return json.dumps([(self.service.getSalarioEspecifico(db, request.id_salario)).toDict()])

    def create_salario(self,db:Session, request:requestSalario):
        if self.service.createSalario(db, request):
            return responseSalario("200","Ok","Salario criado com sucesso")
        return responseSalario("400","Erro","Erro na criacao de salario")

    def remove_salario(self,db:Session, request:requestSalario):
        if self.service.removeSalario(db, request.id_salario):
            return responseSalario("200","Ok","Salario removido com sucesso")
        return responseSalario("400","Erro","Erro na remocao de salario")

    def update_salario(self,db:Session, request:requestSalario):
        if self.service.updateSalario(db, request.id_salario, request.data_salario,request.valor_por_item,request.quantidade_salario,request.banco_depositado,request.CPF_funcionario):
            return responseSalario("200","Ok","Salario atualizado com sucesso")
        return responseSalario("400","Erro","Erro na atualizacao de salario")
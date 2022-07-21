from sqlalchemy.orm import Session
from app.schemas import salarioSchema
import pandas as pd
import json 
from app.services._base import BaseService
from app.config import Sessionlocal
from app.model import salario
from app.config import engine
#from app.config import conn

class salarioService(BaseService):
    def __init__(self) -> None:
        super().__init__()

    def getSalarios(self, db:Session, skip:int=0, limit:int=100):
        resultado=db.query(salario).offset(skip).limit(limit).all()
        return resultado
        # json.dumps([obj.toDict() for obj in resultado])

    def getSalarioEspecifico(self, db:Session, CPF_salario:str):
        resultado = db.query(salario).filter(salario.CPF_salario == CPF_salario).first()
        if resultado is None:
            resultado = []
        return resultado

    def createSalario(self, db:Session, Salario:salarioSchema):
      try:
        _salario = salario(nome_salario=Salario.nome_salario, salario_fixo=Salario.salario_fixo,data_admissao=Salario.data_admissao,eh_gerente=Salario.eh_gerente,comissao_venda=Salario.comissao_venda)
        db.add(_salario)
        db.commit()
        db.refresh(_salario)
        return True
      except:
        return False

    def removeSalario(self,db:Session, id_salario:str):
      try:
        _salario = self.getSalarioEspecifico(db,id_salario)
        db.delete(_salario)
        db.commit()
        return True
      except:
        return False

    def updateSalario(self,db:Session, id_salario, data_salario,valor_por_item,quantidade_salario,banco_depositado,CPF_funcionario):
      try:
        _salario= self.getSalarioEspecifico(db, id_salario)
        _salario.data_salario = data_salario
        _salario.valor_por_item=valor_por_item
        _salario.quantidade_salario=quantidade_salario
        _salario.banco_depositado=banco_depositado
        _salario.CPF_funcionario=CPF_funcionario
        db.commit()
        db.refresh(_salario)
        return True
      except:
        return False
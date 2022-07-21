from datetime import date
from sqlalchemy.orm import Session
from app.schemas import funcionarioSchema
import pandas as pd
import json 
from app.services._base import BaseService
from app.config import Sessionlocal
from app.model import funcionario
from app.config import engine
#from app.config import conn

class funcionarioService(BaseService):
    def __init__(self) -> None:
        super().__init__()

    def getFuncionarios(self, db:Session, skip:int=0, limit:int=100):
        resultado=db.query(funcionario).offset(skip).limit(limit).all()
        return resultado
        # json.dumps([obj.toDict() for obj in resultado])

    def getFuncionarioEspecifico(self, db:Session, CPF_Funcionario:str):
        resultado = db.query(funcionario).filter(funcionario.CPF_Funcionario == CPF_Funcionario).first()
        if resultado is None:
            resultado = []
        return resultado

    def createFuncionario(self, db:Session, Funcionario:funcionarioSchema):
      try:
        _Funcionario = funcionario(CPF_Funcionario=Funcionario.CPF_funcionario,nome_funcionario=Funcionario.nome_funcionario, salario_fixo=Funcionario.salario_fixo,data_admissao=Funcionario.data_admissao,eh_gerente=Funcionario.eh_gerente,comissao_venda=Funcionario.comissao_venda)
        db.add(_Funcionario)
        db.commit()
        db.refresh(_Funcionario)
        return True
      except:
        return False

    def removeFuncionario(self,db:Session, CPF_Funcionario:str):
      try:
        _Funcionario = self.getFuncionarioEspecifico(db,CPF_Funcionario)
        db.delete(_Funcionario)
        db.commit()
        return True
      except:
        return False

    def updateFuncionario(self,db:Session, CPF_funcionario:str, nome_funcionario: str,salario_fixo:str,data_admissao:date,eh_gerente:bool,comissao_venda:float):
      try: 
        _Funcionario= self.getFuncionarioEspecifico(db, CPF_funcionario)
        _Funcionario.nome_funcionario = nome_funcionario
        _Funcionario.salario_fixo = salario_fixo
        _Funcionario.data_admissao = data_admissao
        _Funcionario.eh_gerente=eh_gerente
        _Funcionario.comissao_venda=comissao_venda
        db.commit()
        db.refresh(_Funcionario)
        return True
      except:
        return False
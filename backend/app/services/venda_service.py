from datetime import date
from sqlalchemy.orm import Session
from app.schemas import vendaSchema, compra_venda_ProdutoSchema
import pandas as pd
import json 
from app.services._base import BaseService
from app.config import Sessionlocal
from app.model import venda
from app.config import engine

#from app.config import conn

class vendaService(BaseService):
    def __init__(self) -> None:
        super().__init__()

    def getVendas(self, db:Session, skip:int=0, limit:int=100):
        resultado=db.query(venda).offset(skip).limit(limit).all()
        return resultado
        # json.dumps([obj.toDict() for obj in resultado])

    def getVendaEspecifico(self, db:Session, data=date):
        resultado = db.query(venda).filter(venda.data_venda == data).first()
        if resultado is None:
            resultado = []
        return resultado

    def createVenda(self, db:Session, Venda:vendaSchema, Produto:compra_venda_ProdutoSchema):
      try:
        _venda = venda(data_compra = date.today(),
                              quantidade_compra = Produto.quantidade,
                              valor_por_item = Produto.valor,
                              codigo_produto = Produto.codigo_produto,
                              CPF_funcionario = Venda.CPF_funcionario,
                              CNPJ_fornecedor = Venda.CPF_cliente)
        db.add(_venda)
        db.commit()
        db.refresh(_venda)
        return True
      except:
        return False

    def removeVenda(self,db:Session, id_venda:str):
      try:
        _venda = self.getVendaEspecifico(db,id_venda)
        db.delete(_venda)
        db.commit()
        return True
      except:
        return False

    def updateVenda(self,db:Session, id_venda, data_venda,valor_por_item,quantidade_venda):
      try:
        _venda= self.getVendaEspecifico(db, id_venda)
        _venda.data_venda = data_venda
        _venda.valor_por_item=valor_por_item
        _venda.quantidade_venda=quantidade_venda
        db.commit()
        db.refresh(_venda)
        return True
      except:
        return False
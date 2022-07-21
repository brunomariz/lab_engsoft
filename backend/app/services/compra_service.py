from sqlalchemy.orm import Session
from sqlalchemy.sql import select
from app.model import compra
from app.schemas import compraSchema , compra_venda_ProdutoSchema
from app.services._base import BaseService
from datetime import date

class CompraService(BaseService):
    def __init__(self) -> None:
        super().__init__()

    def getCompras(self, db:Session, skip:int=0, limit:int=100):
        resultado=db.query(compra).offset(skip).limit(limit).all()
        return resultado

    def getCompra_byId(self, db:Session, id: int):
        resultado = db.query().filter(compra.id_compra == id).first()
        if resultado is None:
            return None
        return resultado

    def getCompras_byData(self, db:Session, data: date):
        resultado = db.query().filter(compra.data_compra == data).all()
        if resultado is None:
            return None
        return resultado

    def createCompra(self, db:Session, Compra : compraSchema, Produto : compra_venda_ProdutoSchema):

        try:

            _compra= compra(data_compra = date.today(),
                              quantidade_compra = Produto.quantidade,
                              valor_por_item = Produto.valor,
                              codigo_produto = Produto.codigo_produto,
                              CPF_funcionario = Compra.CPF_funcionario,
                              CNPJ_fornecedor = Compra.CNPJ_fornecedor)
        

            db.add(_compra)
            db.commit()
            db.refresh(_compra)
            return True
        except Exception as e:
            print(e)
            return False

    def removeCompra(self, db:Session, codigo : int):
        _compra = self.getCompra_byId(db,codigo)
        try:
            db.delete(_compra)
            db.commit()
            return True
        except Exception as e:
            print(e)
            return False
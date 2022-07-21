from sqlalchemy.orm import Session
from sqlalchemy.sql import select
from app.model import produto
from app.schemas import produtoSchema
from app.services._base import BaseService
from app.config import Sessionlocal
from app.config import engine

class ProdutoService(BaseService):
    def __init__(self) -> None:
        super().__init__()

    def getProdutos(self, db:Session, skip:int=0, limit:int=100):
        resultado=db.query(produto).offset(skip).limit(limit).all()
        return resultado

    def getProduto_byCodigo(self, db:Session, codigo: int):
        resultado = db.query(produto).filter(produto.codigo_produto == codigo).first()
        if resultado is None:
            return None
        return resultado

    def createProduto(self, db:Session, Produto):
        _produto= produto(nome_produto= Produto.nome_produto,
                          quantidade_produto = Produto.quantidade_produto,
                          em_promocao = Produto.em_promocao,
                          preco_venda = Produto.preco_venda)
        try:
            db.add(_produto)
            db.commit()
            db.refresh(_produto)
            return True
        except Exception as e:
            print(e)
            return False

    def removeProduto(self, db:Session, codigo : int):
        _produto = self.getProduto_byCodigo(db,codigo)
        try:
            db.delete(_produto)
            db.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def setQuantidadeProduto(self, db:Session, codigo : int ,quantidade:int):
        _produto = self.getProduto_byCodigo(db, codigo)

        if _produto is None or  _produto.quantidade_produto + quantidade <0:
            return False
        try:
            _produto.quantidade_produto += quantidade

            db.commit()
            db.refresh(_produto)
            return True
        except Exception as e:
            print(e)
            return False

    def setEmPromocao(self, db:Session, codigo: int , emPromocao : bool):
        _produto = self.getProduto_byCodigo(db, codigo)
        try:
            _produto.em_promocao = emPromocao
            db.commit()
            db.refresh(_produto)
            return True
        except Exception as e:
            print(e)
            return False

    def setPreco(self, db:Session, codigo : int, preco : float):

        _produto = self.getProduto_byCodigo(db, codigo)
        if preco<0:
            return False
        try:
            _produto.preco_venda = preco
            db.commit()
            db.refresh(_produto)
            return True
        except Exception as e:
            print(e)
            return False

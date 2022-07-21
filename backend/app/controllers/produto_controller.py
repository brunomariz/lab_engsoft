from app.controllers._base import BaseController
from sqlalchemy.orm import Session
from app.schemas import requestProduto, requestQuantidadeProduto, requestPromocaoProduto,requestPrecoProduto
from app.services.produto_service import ProdutoService


# Session.query

class ProdutoController(BaseController):
    def __init__(self, service=...) -> None:
        super().__init__(ProdutoService())

    def getProdutos(self,db:Session):
        produtos =  self.service.getProdutos(db)
        if produtos is not None:
            return [produto.toDict() for produto in produtos]
        return
    
    def getPrduto_byCodigo(self,db:Session, codigo : int):
        produto =  self.service.getProduto_byCodigo(db, codigo)
        if produto is not None:
            return [produto.toDict()]
        return
    
    def createProduto(self,db:Session, request : requestProduto):
        return self.service.createProduto(db, request)

    def remove_produto(self,db:Session, codigo: int):
        return self.service.removeProduto(db, codigo)

    def addQuantidadeProduto(self, db:Session, request: requestQuantidadeProduto):
        return self.service.addQuantidadeProduto(db, request.codigo, request.quantidade)

    def setPromocaoProduto(self, db:Session, request: requestPromocaoProduto):
        return self.service.setEmPromocao(db, request.codigo, request.emPromocao)

    def setPrecoProduto(self, db:Session, request: requestPrecoProduto):
        return self.service.setPreco(db, request.codigo, request.preco)
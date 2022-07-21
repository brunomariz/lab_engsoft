from app.controllers._base import BaseController
from sqlalchemy.orm import Session
from app.schemas import requestCompra
from app.services.compra_service import CompraService
from datetime import date
from app.services.produto_service import ProdutoService
# Session.query

class CompraController(BaseController):
    def __init__(self, service=...) -> None:
        super().__init__(CompraService())

    def getCompras(self, db: Session):
        compras = self.service.getCompras(db)
        if compras is not None:
            return [compra.toDict() for compra in compras]
        return []

    def getCompra_byId(self, db: Session, id: int):
        compra = self.service.getCompra_byId(db, id)
        if compra is not None:
            return [compra.toDict()]
        return []

    def getCompras_byData(self, db: Session, data: date):
        compra = self.service.getCompra_byData(db, data)
        if compra is not None:
            return [compra.toDict()]
        return []

    def createCompra(self, db: Session, request: requestCompra):

        produto_service = ProdutoService()
        completed = []
        for produto in request.produtos:
            try:
                ok = produto_service.addQuantidadeProduto(db, produto.codigo_produto,
                                                        abs(produto.quantidade))
                if not ok:
                    continue
                completed.append(self.service.createCompra(db, request, produto))
            except Exception as e:
                print(e)
                return False
        return len(completed) == len(request.produtos)

    def remove_compra(self, db: Session, id: int):
        return self.service.removeCompra(db, id)

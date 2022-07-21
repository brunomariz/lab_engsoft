from app.controllers._base import BaseController
from sqlalchemy.orm import Session
from app.schemas import compraSchema
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

    def createCompra(self, db: Session, request: compraSchema):
        produto_service = ProdutoService()
        try:
            ok = produto_service.setQuantidadeProduto(db, request.codigo_produto,
                                                    abs(request.quantidade_compra))
            if not ok:
                return False
            return self.service.createCompra(db, request)
        except Exception as e:
            print(e)
            return False

    def remove_compra(self, db: Session, id: int):
        return self.service.removeCompra(db, id)

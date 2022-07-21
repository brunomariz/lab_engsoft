from app.controllers._base import BaseController
from sqlalchemy.orm import Session
from app.schemas import vendaSchema, requestVenda, responseVenda
from app.services.venda_service import vendaService
from app.services.produto_service import ProdutoService
import json
from datetime import date
# Session.query

class vendaController(BaseController):
    def __init__(self, service=...) -> None:
        super().__init__(vendaService())

    def getVendas(self, db: Session):
        vendas = self.service.getVendas(db)
        if vendas is not None:
            return [compra.toDict() for compra in vendas]
        return []

    # def getCompra_byId(self, db: Session, id: int):
    #     compra = self.service.getCompra_byId(db, id)
    #     if compra is not None:
    #         return [compra.toDict()]
    #     return []

    # def getCompras_byData(self, db: Session, data: date):
    #     compra = self.service.getCompra_byData(db, data)
    #     if compra is not None:
    #         return [compra.toDict()]
    #     return []


    def get_vendaEspecifico(self,db:Session, request: requestVenda):
        return [(self.service.getVendaEspecifico(db, request.id_venda)).toDict()]

    def create_venda(self,db:Session, request:requestVenda):
        produto_service = ProdutoService()
        completed = []
        for produto in request.produtos:
            try:
                ok = produto_service.addQuantidadeProduto(db, produto.codigo_produto,-produto.quantidade)
                if not ok:
                    continue
                completed.append(self.service.createVenda(db, request, produto))
            except Exception as e:
                print(e)
                return False
        return len(completed) == len(request.produtos)

    def remove_venda(self,db:Session, request:requestVenda):
        if self.service.removevenda(db, request.id_venda):
            ProdutoService.addQuantidadeProduto(db=db,codigo=request.codigo_produto,quantidade=int(request.quantidade_venda))
            return responseVenda("200","Ok","Venda removido com sucesso")
        return responseVenda("400","Erro","Erro na remocao de venda")

    def update_venda(self,db:Session, request:requestVenda):
        if self.service.updateVenda(db, request.id_venda, request.data_venda,request.valor_por_item,request.quantidade_venda,request.banco_depositado,request.CPF_funcionario):
            return responseVenda("200","Ok","Venda atualizada com sucesso")
        return responseVenda("400","Erro","Erro na atualizacao de venda")
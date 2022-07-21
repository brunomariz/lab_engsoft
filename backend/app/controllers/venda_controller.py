from app.controllers._base import BaseController
from sqlalchemy.orm import Session
from app.schemas import vendaSchema, requestVenda, responseVenda
from app.services.venda_service import vendaService
from app.services.produto_service import ProdutoService
import json
# Session.query

class vendaController(BaseController):
    def __init__(self, service=...) -> None:
        super().__init__(vendaService())

    def get_vendas(self,db:Session):
        return [obj.toDict() for obj in self.service.getvendas(db)]

    def get_vendaEspecifico(self,db:Session, request: requestVenda):
        return [(self.service.getvendaEspecifico(db, request.id_venda)).toDict()]

    def create_venda(self,db:Session, request:requestVenda):
        if self.service.createVenda(db, request):
            ProdutoService.addQuantidadeProduto(db=db,codigo=request.codigo_produto,quantidade=-int(request.quantidade_venda))
            return responseVenda("200","Ok","Venda criado com sucesso")
        return responseVenda("400","Erro","Erro na criacao de venda")

    def remove_venda(self,db:Session, request:requestVenda):
        if self.service.removevenda(db, request.id_venda):
            ProdutoService.addQuantidadeProduto(db=db,codigo=request.codigo_produto,quantidade=int(request.quantidade_venda))
            return responseVenda("200","Ok","Venda removido com sucesso")
        return responseVenda("400","Erro","Erro na remocao de venda")

    def update_venda(self,db:Session, request:requestVenda):
        if self.service.updateVenda(db, request.id_venda, request.data_venda,request.valor_por_item,request.quantidade_venda,request.banco_depositado,request.CPF_funcionario):
            return responseVenda("200","Ok","Venda atualizada com sucesso")
        return responseVenda("400","Erro","Erro na atualizacao de venda")
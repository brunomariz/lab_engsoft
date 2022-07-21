from sqlalchemy import Column, Integer, String, VARCHAR, Date, Numeric, ForeignKey, ColumnDefault, Boolean
from app.config import Base
from datetime import date

def _toDict(obj):
    aux = obj.__dict__
    delete = []
    for key in aux.keys():
        val = aux[key]
        if not isinstance(val, (str, int, bool, float, date)):
            delete.append(key)
    for key in delete:
        del aux[key]
    return aux


class cliente(Base):
    __tablename__ = 'Cliente'
    CPF_cliente=Column(VARCHAR, primary_key=True)
    nome_cliente=Column(VARCHAR)

    def toDict(self):
        return _toDict(self)

class funcionario(Base):
    __tablename__ = 'Funcionario'
    CPF_funcionario=Column(VARCHAR, primary_key=True)
    nome_funcionario=Column(VARCHAR)
    salario_fixo=Column(Integer)
    data_admissao=Column(Date)
    eh_gerente=Column(Boolean)
    comissao_venda=Column(Numeric)
    login_usuario=Column(VARCHAR)


    def toDict(self):
       return _toDict(self)

class fornecedor(Base):
    __tablename__ = 'Fornecedor'
    CNPJ_fornecedor=Column(VARCHAR, primary_key=True)
    nome_fornecedor=Column(VARCHAR)

    def toDict(self):
       return _toDict(self)

class produto(Base):
    __tablename__ = 'Produto'
    codigo_produto=Column(Integer, primary_key=True)
    nome_produto=Column(VARCHAR)
    quantidade_produto=Column(Integer, default=0)
    em_promocao=Column(Boolean,default=False)
    preco_venda=Column(Numeric)

    def toDict(self):
       return _toDict(self)

class venda(Base):
    __tablename__ = 'Venda'
    id_venda=Column(Integer, primary_key=True)
    data_venda=Column(Date)
    valor_por_item=Column(Numeric)
    quantidade_venda=Column(Integer,default=1)

    codigo_produto=Column(Integer,ForeignKey('Produto.codigo_produto'), nullable=False)
    CPF_funcionario=Column(String,ForeignKey('Funcionario.CPF_funcionario'), nullable=False)
    CNPJ_forcenedor=Column(String,ForeignKey('CNPJ_fornecedor'), nullable=False)


    def toDict(self):
       return _toDict(self)

class compra(Base):
    __tablename__ = 'Compra'
    id_compra=Column(Integer, primary_key=True)
    data_compra=Column(Date)
    valor_por_item=Column(Numeric)
    quantidade_compra=Column(Integer, default=1)

    codigo_produto=Column(Integer,ForeignKey('Produto.codigo_produto', ondelete='CASCADE'), nullable=False)
    CPF_funcionario=Column(String,ForeignKey('Funcionario.CPF_funcionario', ondelete='CASCADE'), nullable=False)
    CNPJ_fornecedor=Column(String,ForeignKey('Fornecedor.CNPJ_fornecedor', ondelete='CASCADE'), nullable=False)

    def toDict(self):
        return _toDict(self)

class salario(Base):
    __tablename__ = 'Salario'
    id_salario=Column(Integer, primary_key=True)
    data_salario=Column(Date)
    valor_por_item=Column(Numeric)
    quantidade_salario=Column(Integer, default=1)
    banco_depositado=Column(String)

    CPF_funcionario=Column(String,ForeignKey('Funcionario.CPF_funcionario'), nullable=False)


    def toDict(self):
       return _toDict(self)

class usuario(Base):
    __tablename__ = 'Usuario'
    login=Column(String,primary_key=True)
    senha=Column(VARCHAR)
    eh_admin=Column(Boolean)


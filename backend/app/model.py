from sqlalchemy import Column, Integer, String, VARCHAR, Date, Numeric, ForeignKey, ColumnDefault, Boolean
from app.config import Base
from sqlalchemy.orm import relationship

class cliente(Base):
    __tablename__ = 'Cliente'
    CPF_cliente=Column(VARCHAR, primary_key=True)
    nome_cliente=Column(VARCHAR)

class funcionario(Base):
    __tablename__ = 'Funcionario'
    CPF_funcionario=Column(VARCHAR, primary_key=True)
    nome_funcionario=Column(VARCHAR)
    salario_fixo=Column(Integer)
    data_admissao=Column(Date)
    eh_gerente=Column(Boolean)
    comissao_venda=Column(Numeric)
    login_usuario=Column(VARCHAR)

class fornecedor(Base):
    __tablename__ = 'Fornecedor'
    CNPJ_fornecedor=Column(VARCHAR, primary_key=True)
    nome_fornecedor=Column(VARCHAR)

class produto(Base):
    __tablename__ = 'Produto'
    codigo_produto=Column(Integer, primary_key=True)
    nome_produto=Column(VARCHAR)
    quantidade_produto=Column(Integer, default=0)
    em_promocao=Column(Boolean)

class venda(Base):
    __tablename__ = 'Venda'
    id_venda=Column(Integer, primary_key=True)
    data_venda=Column(Date)
    valor_por_item=Column(Numeric)
    quantidade_venda=Column(Integer,default=1)

    codigo_produto=Column(Integer,ForeignKey('Produto.codigo_produto', ondelete='CASCADE'), nullable=False)
    CPF_funcionario=Column(String,ForeignKey('Funcionario.CPF_funcionario', ondelete='CASCADE'), nullable=False)
    CPF_cliente=Column(String,ForeignKey('Cliente.CPF_cliente', ondelete='CASCADE'), nullable=False)

    produto = relationship('Produto', backref='Venda')
    funcionario = relationship('Funcionario', backref='Venda')
    cliente = relationship('Cliente', backref='Venda')

class compra(Base):
    __tablename__ = 'Compra'
    id_compra=Column(Integer, primary_key=True)
    data_compra=Column(Date)
    valor_por_item=Column(Numeric)
    quantidade_compra=Column(Integer, default=1)

    codigo_produto=Column(Integer,ForeignKey('Produto.codigo_produto', ondelete='CASCADE'), nullable=False)
    CPF_funcionario=Column(String,ForeignKey('Funcionario.CPF_funcionario', ondelete='CASCADE'), nullable=False)
    CPF_cliente=Column(String,ForeignKey('Cliente.CPF_cliente', ondelete='CASCADE'), nullable=False)

    produto = relationship('Produto', backref='Compra')
    funcionario = relationship('Funcionario', backref='Compra')
    cliente = relationship('Cliente', backref='Compra')

class salario(Base):
    __tablename__ = 'Salario'
    id_salario=Column(Integer, primary_key=True)
    data_salario=Column(Date)
    valor_por_item=Column(Numeric)
    quantidade_salario=Column(Integer, default=1)
    banco_depositado=Column(String)

    CPF_funcionario=Column(String,ForeignKey('Funcionario.CPF_funcionario', ondelete='CASCADE'), nullable=False)

    funcionario = relationship('Funcionario', backref='Salario')




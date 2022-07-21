from datetime import date
from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar('T')

class clienteSchema(BaseModel):
    CPF_cliente: str
    nome_cliente: Optional[str]

    class config:
        orm_mode = True

class requestCliente(BaseModel):
    CPF_cliente: str
    nome_cliente: Optional[str]

class responseCliente(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]

class usuarioSchema(BaseModel):
    login: str
    senha:str
    eh_admin:bool=False

    class config:
        orm_mode = True

class requestUsuario(BaseModel):
    login: str
    senha:str
    eh_admin:bool=False

class responseUsuario(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]

class funcionarioSchema(BaseModel):
    CPF_funcionario: str
    nome_funcionario: Optional[str]
    salario_fixo: float
    data_admissao: date
    eh_gerente: Optional[bool]=False
    comissao_venda:Optional[float]=0.1

    login_usuario:str
    class config:
        orm_mode = True

class requestFuncionario(BaseModel):
    CPF_funcionario: str
    nome_funcionario: Optional[str]
    salario_fixo: float
    data_admissao: date
    eh_gerente: Optional[bool]=False
    comissao_venda:Optional[float]=0.1

    login_usuario:str

class responseFuncionario(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]

class fornecedorSchema(BaseModel):
    CNPJ_fornecedor: str
    nome_fornecedor: Optional[str]

    class config:
        orm_mode = True

class requestFornecedor(BaseModel):
    CNPJ_fornecedor: str
    nome_fornecedor: Optional[str]

class responseFornecedor(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]

class produtoSchema(BaseModel):
    codigo_produto: int
    nome_produto: str
    quantidade_produto: int=0
    em_promocao:Optional[bool]=False
    preco_venda=float

    class config:
        orm_mode = True

class requestProduto(BaseModel):
    codigo_produto: int
    nome_produto: str
    quantidade_produto: int=0
    em_promocao:Optional[bool]=False
    preco_venda=float

class responseProduto(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]

class salarioSchema(BaseModel):
    id_salario: int
    data_salario: date
    valor_por_item:float
    quantidade_salario: int=1
    banco_depositado:str
    
    CPF_funcionario: str
    
    class config:
        orm_mode = True

class requestSalario(BaseModel):
    id_salario: int
    data_salario: date
    valor_por_item:float
    quantidade_salario: int=1
    banco_depositado:str
    
    CPF_funcionario: str

class responseSalario(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]

class compraSchema(BaseModel):
    id_compra: int
    data_compra: date
    valor_por_item:float
    quantidade_compra: int=1

    codigo_produto: int
    CPF_funcionario: str
    CNPJ_fornecedor: str
    
    class config:
        orm_mode = True

class requestCompra(BaseModel):
    id_compra: int
    data_compra: date
    valor_por_item:float
    quantidade_compra: int=1

    codigo_produto: int
    CPF_funcionario: str
    CNPJ_fornecedor: str
    

class responseCompra(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]

class vendaSchema(BaseModel):
    id_venda: int
    data_venda: date
    valor_por_item:float
    quantidade_venda: int=1

    codigo_produto: int
    CPF_funcionario: str
    CPF_cliente: str
    
    class config:
        orm_mode = True

class requestVenda(BaseModel):
    id_venda: int
    data_venda: date
    valor_por_item:float
    quantidade_venda: int=1

    codigo_produto: int
    CPF_funcionario: str
    CPF_cliente: str

class responseVenda(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]
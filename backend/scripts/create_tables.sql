
CREATE TABLE Usuario(
	login VARCHAR(50),
	senha VARCHAR(64) NOT NULL,
	eh_admin BOOLEAN DEFAULT false,

	PRIMARY KEY(login)
);


CREATE TABLE Funcionario(
	CPF_funcionario VARCHAR(11),
	nome_funcionario VARCHAR(30) NOT NULL,
	salario_fixo NUMERIC(30) NOT NULL,
	data_admissao DATE NOT NULL,
	eh_gerente BOOLEAN DEFAULT false,
	comissao_venda real default 0.1,

	login_usuario VARCHAR(50) NOT NULL,

	primary KEY(CPF_funcionario)
);


CREATE TABLE Produto(
	codigo_produto NUMERIC(50),
	nome_produto VARCHAR(50) NOT NULL,
	quantidade_produto INT DEFAULT 0,
	em_promocao BOOLEAN DEFAULT false,
	preco_venda NUMERIC NOT NULL,

	PRIMARY KEY(codigo_produto)
);


CREATE TABLE Salario(
	id_salario BIGSERIAL not NULL,
	data_salario DATE NOT NULL,
	valor_por_item NUMERIC(6,2) NOT NULL,
	quantidade_salario INT DEFAULT 1,
	banco_depositado VARCHAR(30) NOT NULL,
    
	CPF_funcionario VARCHAR(11) NOT NULL,

	PRIMARY KEY(id_salario)
);


CREATE TABLE Compra(
	id_compra BIGSERIAL not NULL,
	data_compra DATE NOT NULL,
	valor_por_item NUMERIC NOT NULL,
	quantidade_compra INT DEFAULT 1,

	codigo_produto NUMERIC NOT NULL,
	CPF_funcionario VARCHAR(11) NOT NULL,
	CNPJ_fornecedor VARCHAR(14) NOT NULL,

	PRIMARY KEY(id_compra)

);


CREATE TABLE Venda(
	id_venda BIGSERIAL not null,
	data_venda DATE NOT NULL,
	valor_por_item NUMERIC NOT NULL,
	quantidade_venda INT DEFAULT 1,

	codigo_produto NUMERIC NOT NULL,
	CPF_funcionario VARCHAR(11) NOT NULL,
	CPF_cliente VARCHAR(11) NOT NULL,

	PRIMARY KEY(id_venda)
);


CREATE TABLE Fornecedor(
	CNPJ_fornecedor VARCHAR(14) NOT NULL,
	nome_fornecedor VARCHAR(30) not null,

	PRIMARY KEY(CNPJ_fornecedor)
);

CREATE TABLE Cliente(
	CPF_cliente VARCHAR(11) NOT NULL,
	nome_cliente VARCHAR(30) not null,
   
	PRIMARY KEY(CPF_cliente)
);


ALTER TABLE Funcionario ADD Foreign Key(login_usuario) REFERENCES Usuario;

ALTER TABLE Salario ADD Foreign Key(CPF_funcionario) REFERENCES Funcionario;

ALTER TABLE Compra ADD Foreign Key(codigo_produto) REFERENCES Produto;
ALTER TABLE Compra ADD Foreign Key(CPF_funcionario) REFERENCES Funcionario;
ALTER TABLE Compra ADD Foreign Key(CNPJ_fornecedor) REFERENCES Fornecedor;

ALTER TABLE Venda ADD Foreign Key(codigo_produto) REFERENCES Produto;
ALTER TABLE Venda ADD Foreign Key(CPF_funcionario) REFERENCES Funcionario;
ALTER TABLE Venda ADD Foreign Key(CPF_cliente) REFERENCES Cliente;

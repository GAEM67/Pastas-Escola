create database ecommerce;
use ecommerce;
CREATE TABLE cliente(
    id INT PRIMARY KEY IDENTITY,
	nome VARCHAR(100) NOT NULL,
	cidade VARCHAR(50),
	data_nascimento DATE,
	Data_cadastro DATE,
    sexo CHAR(1),
    limite_credito numeric(10,2),
	email VARCHAR(100),
	senha VARCHAR(50)
);

CREATE TABLE produto(
    Id_produto INT PRIMARY KEY IDENTITY,
    nome VARCHAR(100) NOT NULL,
    categoria VARCHAR(50),
    preco numeric(10,2),
	estoque int,
	data_cadastro date);

CREATE TABLE pedido(
    id_pedido INT PRIMARY KEY IDENTITY,
    valor_total decimal(10,2),
    id_cliente INT,
	data_pedido DATE,
	status varchar(30),
	forma_pagamento varchar(30),
	FOREIGN KEY (id_cliente) REFERENCES cliente(id)
);

INSERT INTO cliente
(nome, cidade, data_nascimento, data_cadastro, sexo, limite_credito, email, senha)
VALUES
('João Silva', 'São Paulo', '1990-05-10', '2024-01-15', 'M', 5000.00, 'joao@email.com', '123'),
('Maria Souza', 'Rio de Janeiro', '1988-11-20', '2024-02-10', 'F', 8000.00, 'maria@email.com', '123'),
('Pedro Santos', 'São Paulo', '1995-07-08', '2024-03-05', 'M', 3000.00, 'pedro@email.com', '123'),
('Ana Costa', 'Belo Horizonte', '1992-09-15', '2024-03-20', 'F', 7000.00, 'ana@email.com', '123'),
('Carlos Lima', 'Curitiba', '1985-01-30', '2024-04-12', 'M', 10000.00, 'carlos@email.com', '123');

INSERT INTO produto
(nome, categoria, preco, estoque, data_cadastro)
VALUES
('Notebook Dell', 'Informática', 3500.00, 20, '2024-01-10'),
('Mouse Gamer', 'Informática', 150.00, 100, '2024-01-10'),
('Teclado Mecânico', 'Informática', 300.00, 50, '2024-01-12'),
('Smartphone Samsung', 'Telefonia', 2500.00, 30, '2024-02-05'),
('Fone Bluetooth', 'Telefonia', 200.00, 80, '2024-02-10'),
('Cadeira Gamer', 'Móveis', 1200.00, 15, '2024-03-01');

INSERT INTO pedido
(valor_total, id_cliente, data_pedido, status, forma_pagamento)
VALUES
(3650.00, 1, '2024-05-01', 'Entregue', 'Cartão'),
(2500.00, 2, '2024-05-02', 'Entregue', 'PIX'),
(200.00, 2, '2024-05-05', 'Entregue', 'PIX'),
(1200.00, 3, '2024-05-06', 'Pendente', 'Boleto'),
(3800.00, 1, '2024-05-10', 'Entregue', 'Cartão'),
(150.00, 4, '2024-05-12', 'Cancelado', 'PIX'),
(300.00, 5, '2024-05-15', 'Entregue', 'Cartão'),
(2500.00, 3, '2024-05-18', 'Entregue', 'PIX');


SELECT LOWER(NOME), LOWER(CATEGORIA) FROM PRODUTO
SELECT NOME, LEN(NOME), SUBSTRING(EMAIL,1,5) + DATA_NASCIMENTO AS 'SUGESTÃO DE SENHA' FROM CLIENTE;
SELECT NOME, SUBSTRING(NOME, 1, 3) FROM PRODUTO;
SELECT NOME, PRECO, (PRECO/100)*85 AS PRECO_DESCONTO FROM PRODUTO;
SELECT LOCALDATE - DATA_PEDIDO FROM PEDIDO
SELECT LEN(id_pedido), SUM(VALOR_TOTAL), AVG(VALOR_TOTAL), MAX(VALOR_TOTAL), MIN(VALOR_TOTAL) FROM PEDIDO;
SELECT COUNT(ID), cidade FROM cliente GROUP BY cidade;
SELECT SUM(estoque) / 2, SUM(PRECO), AVG(PRECO), MAX(PRECO), categoria FROM PRODUTO GROUP BY CATEGORIA;
SELECT LEN(id_PEDIDO), SUM(VALOR_TOTAL) FROM PEDIDO ORDER BY FORMA_PAGAMENTO;
SELECT DATA_PEDIDO, DATA_PEDIDO + 7 AS PRAZO_ENTREGA FROM PEDIDO;

select * from pedido;
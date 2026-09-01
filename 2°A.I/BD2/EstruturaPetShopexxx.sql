Create database PetShop;
use PetShop;


CREATE TABLE Cliente1 (
    cliente_id INT PRIMARY KEY IDENTITY,
    nome VARCHAR(100),
    telefone VARCHAR(20),
    email VARCHAR(100),
    data_cadastro DATE
);

CREATE TABLE Servico1 (
    servico_id INT PRIMARY KEY IDENTITY,
    nome VARCHAR(100),
    preco DECIMAL(10,2),
    duracao_minutos INT
);

CREATE TABLE Animal (
    animal_id INT PRIMARY KEY IDENTITY,
    nome VARCHAR(50),
    especie VARCHAR(50),
    raca VARCHAR(50),
    idade INT,
    cliente_id INT,
    FOREIGN KEY (cliente_id) REFERENCES Cliente1(cliente_id)
);

CREATE TABLE Funcionario (
    funcionario_id INT PRIMARY KEY IDENTITY,
    nome VARCHAR(100),
    cargo VARCHAR(50),
    salario DECIMAL(10,2),
    data_contratacao DATE
);


CREATE TABLE Animal_Servico (
    animal_id INT,
    servico_id INT,
    data_servico DATETIME,
    funcionario_id INT,
    observacoes TEXT,
    PRIMARY KEY (animal_id, servico_id, data_servico),
    FOREIGN KEY (animal_id) REFERENCES Animal(animal_id),
    FOREIGN KEY (servico_id) REFERENCES Servico(servico_id),
    FOREIGN KEY (funcionario_id) REFERENCES Funcionario(funcionario_id)
);

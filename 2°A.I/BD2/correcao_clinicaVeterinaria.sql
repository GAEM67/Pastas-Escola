-- ===========================================
-- CRIAÇÃO DO BANCO DE DADOS
-- ===========================================

CREATE DATABASE ClinicaVeterinaria;

USE ClinicaVeterinaria;

-- ===========================================
-- CRIAÇÃO DAS TABELAS
-- ===========================================

CREATE TABLE Cliente(
    id_cliente INT IDENTITY PRIMARY KEY,
    nome VARCHAR(100),
    telefone VARCHAR(20),
    cidade VARCHAR(50)
);

CREATE TABLE Animal(
    id_animal INT IDENTITY PRIMARY KEY,
    nome VARCHAR(50),
    especie VARCHAR(30),
    raca VARCHAR(40),
    idade INT,
    id_cliente INT,
    FOREIGN KEY(id_cliente) REFERENCES Cliente(id_cliente)
);

CREATE TABLE Consulta(
    id_consulta INT IDENTITY PRIMARY KEY,
    data_consulta DATE,
    valor DECIMAL(10,2),
    diagnostico VARCHAR(100),
    id_animal INT,
    FOREIGN KEY(id_animal) REFERENCES Animal(id_animal)
);

-- ===========================================
-- INSERTS CLIENTES
-- ===========================================

INSERT INTO Cliente(nome,telefone,cidade)
VALUES
('Ana Souza','11999990001','São Paulo'),
('Bruno Lima','11999990002','Campinas'),
('Carlos Mendes','11999990003','Sorocaba'),
('Daniela Rocha','11999990004','São Paulo'),
('Eduardo Silva','11999990005','Jundiaí');

-- ===========================================
-- INSERTS ANIMAIS
-- ===========================================

INSERT INTO Animal(nome,especie,raca,idade,id_cliente)
VALUES
('Rex','Cachorro','Labrador',8,1),
('Mimi','Gato','Persa',3,2),
('Luna','Cachorro','Poodle',2,3),
('Pingo','Coelho','Mini Lop',4,4),
('Kiara','Ave','Calopsita',1,5);

-- ===========================================
-- INSERTS CONSULTAS
-- ===========================================

INSERT INTO Consulta(data_consulta,valor,diagnostico,id_animal)
VALUES
('2025-03-10',120.00,'Vacinação',1),
('2025-03-15',250.00,'Infecção',2),
('2025-04-01',180.00,'Check-up',3),
('2025-04-20',90.00,'Corte de unhas',4),
('2025-05-05',320.00,'Cirurgia',5);

-- ===========================================
-- RESOLUÇÃO DOS EXERCÍCIOS
-- ===========================================

-- 1 Liste todos os clientes cadastrados.
SELECT * FROM Cliente;

-- 2 Liste todos os animais cadastrados.
SELECT * FROM Animal;

-- 3 Liste todos as consultas cadastrados.
SELECT * FROM Consulta;

-- 4  Mostre os clientes em ordem alfabética de nome.
SELECT * FROM Cliente
ORDER BY nome;

-- 5  Mostre os animais do mais velho para o mais novo.
SELECT * FROM Animal
ORDER BY idade DESC;

-- 6 Liste as consultas da mais barata para a mais cara.
SELECT * FROM Consulta
ORDER BY valor;

-- 7 Mostre os animais cuja espécie seja Cachorro.
SELECT * FROM Animal
WHERE especie='Cachorro';

-- 8 Mostre os clientes que moram na cidade de São Paulo.
SELECT * FROM Cliente
WHERE cidade='São Paulo';

-- 9 Liste os animais que possuem idade maior que 5 anos.

SELECT * FROM Animal
WHERE idade>5;

-- 10 Mostre os clientes que moram em São Paulo OU Campinas.
SELECT * FROM Cliente
WHERE cidade='São Paulo'
OR cidade='Campinas';

-- 11 Mostre os animais que sejam da espécie Gato OU Coelho.
SELECT * FROM Animal
WHERE especie='Gato'
OR especie='Coelho';

-- 12 Liste as consultas com valor maior que R$100 E menor que R$300.
SELECT * FROM Consulta
WHERE valor>100
AND valor<300;

-- 13 Mostre os animais que sejam da espécie Cachorro E tenham mais de 3 anos
SELECT * FROM Animal
WHERE especie='Cachorro'
AND idade>3;

-- 14 Liste os clientes que não moram em São Paulo.
SELECT * FROM Cliente
WHERE NOT cidade='São Paulo';

-- 15  Mostre os animais que não sejam da espécie Cachorro.

SELECT * FROM Animal
WHERE NOT especie='Cachorro';

-- 16  Liste as consultas cujo valor esteja entre R$100 e R$250.
SELECT * FROM Consulta
WHERE valor BETWEEN 100 AND 250;

-- 17 Mostre os animais cuja idade esteja entre 2 e 8 anos.
SELECT * FROM Animal
WHERE idade BETWEEN 2 AND 8;

-- 18 Liste os clientes que moram em São Paulo, Campinas ou Sorocaba.
SELECT * FROM Cliente
WHERE cidade IN ('São Paulo','Campinas','Sorocaba');

-- 19 Mostre os animais cuja espécie seja Cachorro, Gato ou Ave.
SELECT * FROM Animal
WHERE especie IN ('Cachorro','Gato','Ave');

-- 20a Clientes cujo nome começa com a letra A.

SELECT * FROM Cliente
WHERE nome LIKE 'A%';

-- 20b Clientes cujo nome termina com a letra o.
SELECT * FROM Cliente
WHERE nome LIKE '%o';

-- 20c Animais cujo nome contém a letra a.
SELECT * FROM Animal
WHERE nome LIKE '%a%';

-- 20d Clientes cujo nome possui a sequência "an"
SELECT * FROM Cliente
WHERE nome LIKE '%an%';

-- 20e Animais cujo nome termina com "a".
SELECT * FROM Animal
WHERE nome LIKE '%a';

-- 21 Exercício 21 - Liste os animais da espécie Cachorro com idade entre 2 e 8 anos.
SELECT * FROM Animal
WHERE especie = 'cachorro' and idade between 2 and 8;

--Exercício 22 - Liste as consultas com valor entre R$100 e R$300 e diagnóstico diferente de "Vacinação".
select * from Consulta 
where valor between 100 and 300 and diagnostico != 'Vacinação';

--Exercício 23 - Liste os clientes que moram em São Paulo ou Campinas e cujo nome começa com a letra "M".
select * from Cliente
where cidade in('São Paulo', 'Campinas') and nome like 'M%';



USE ClinicaVeterinaria;

-- ==========================================
-- 1. EXEMPLOS COM DISTINCT (Remove repetições)
-- ==========================================

-- Exemplo 1: Listar as cidades únicas onde os clientes moram
SELECT DISTINCT cidade 
FROM Cliente;

-- Exemplo 2: Descobrir quais são as espécies únicas cadastradas
SELECT DISTINCT especie 
FROM Animal;

-- Exemplo 3: Listar os tipos de diagnósticos únicos já dados nas consultas
SELECT DISTINCT diagnostico 
FROM Consulta;


-- ==========================================
-- 2. EXEMPLOS COM GROUP BY (Agrupa dados e faz cálculos)
-- ==========================================

-- Exemplo 1: Contar quantos animais existem de cada espécie
SELECT especie, COUNT(*) AS quantidade_animais 
FROM Animal 
GROUP BY especie;

-- Exemplo 2: Contar quantos clientes residem em cada cidade
SELECT cidade, COUNT(*) AS total_clientes 
FROM Cliente 
GROUP BY cidade;

-- Exemplo 3: Calcular o valor total arrecadado em consultas por cada animal
SELECT id_animal, SUM(valor) AS total_gasto 
FROM Consulta 
GROUP BY id_animal;


-- ==========================================
-- 3. EXEMPLOS COM HAVING (Filtra os grupos criados)
-- ==========================================

-- Exemplo 1: Listar as cidades que possuem MAIS de 1 cliente cadastrado
SELECT cidade, COUNT(*) AS total_clientes 
FROM Cliente 
GROUP BY cidade 
HAVING COUNT(*) > 1;

-- Exemplo 2: Listar os animais (por ID) cujo total gasto em consultas ultrapassa R$ 150,00
SELECT id_animal, SUM(valor) AS total_gasto 
FROM Consulta 
GROUP BY id_animal 
HAVING SUM(valor) > 150.00;

-- Exemplo 3: Listar as espécies cadastradas cuja média de idade seja maior ou igual a 3 anos
SELECT especie, AVG(idade) AS media_idade 
FROM Animal 
GROUP BY especie 
HAVING AVG(idade) >= 3;

-- Exercício 1 Mostre a quantidade total de clientes cadastrados.
SELECT COUNT(*) AS quantidade_clientes
FROM Cliente;

-- Exercício 2 Mostre a quantidade total de animais cadastrados.
SELECT COUNT(*) AS quantidade_animais
FROM Animal;

-- Exercício 3 Mostre a quantidade total de consultas realizadas.
SELECT COUNT(*) AS quantidade_consultas
FROM Consulta;

-- Exercício 4 Calcule o valor total arrecadado com todas as consultas.
SELECT SUM(valor) AS valor_total
FROM Consulta;

-- Exercício 5 Mostre o valor médio das consultas.
SELECT AVG(valor) AS valor_medio
FROM Consulta;

-- Exercício 6 Mostre o maior valor registrado em uma consulta.
SELECT MAX(valor) AS maior_valor
FROM Consulta;

-- Exercício 7 Mostre o menor valor registrado em uma consulta.
SELECT MIN(valor) AS menor_valor
FROM Consulta;

-- Exercício 8 Mostre a idade média dos animais cadastrados.
SELECT AVG(idade) AS idade_media
FROM Animal;

-- Exercício 9 Mostre a idade do animal mais velho.
SELECT MAX(idade) AS maior_idade
FROM Animal;

-- Exercício 10 Mostre a idade do animal mais novo.
SELECT MIN(idade) AS menor_idade
FROM Animal;

-- Exercício 11 Mostre o nome de cada cliente e a quantidade de caracteres do seu nome.
SELECT nome, LEN(nome) AS quantidade_caracteres
FROM Cliente;

-- Exercício 12 Mostre o nome dos animais juntamente com a quantidade de letras do nome.
SELECT nome, LEN(nome) AS quantidade_caracteres
FROM Animal;

-- Exercício 13 Mostre os diagnósticos e o tamanho de cada texto.
SELECT diagnostico, LEN(diagnostico) AS tamanho_texto
FROM Consulta;

-- Exercício 14 Liste apenas os clientes cujo nome possui mais de 10 caracteres.
SELECT *
FROM Cliente
WHERE LEN(nome) > 10;

-- Exercício 15 Liste os animais cujo nome possui exatamente 5 caracteres.
SELECT *
FROM Animal
WHERE LEN(nome) = 5;

-- Exercício 16 Mostre todos os nomes dos clientes em letras maiúsculas.

SELECT UPPER(nome) AS nome_maiusculo
FROM Cliente;

-- Exercício 17 Mostre os nomes dos animais em letras maiúsculas.
SELECT UPPER(nome) AS nome_maiusculo
FROM Animal;

-- Exercício 18 Mostre os diagnósticos escritos totalmente em letras maiúsculas.
SELECT UPPER(diagnostico) AS diagnostico_maiusculo
FROM Consulta;

-- Exercício 19 Mostre os nomes dos clientes em letras minúsculas.
SELECT LOWER(nome) AS nome_minusculo
FROM Cliente;

-- Exercício 20 Mostre a espécie dos animais em letras minúsculas.
SELECT LOWER(especie) AS especie_minuscula
FROM Animal;

-- Exercício 21 Mostre o nome da raça de todos os animais em letras minúsculas.
SELECT LOWER(raca) AS raca_minuscula
FROM Animal;

-- Exercício 22 Mostre os três primeiros caracteres do nome de cada cliente.
SELECT nome, SUBSTRING(nome, 1, 3) AS tres_primeiros
FROM Cliente;

-- Exercício 23 Mostre os quatro primeiros caracteres do nome de cada animal.
SELECT nome, SUBSTRING(nome, 1, 4) AS quatro_primeiros
FROM Animal;

-- Exercício 24 Mostre os cinco primeiros caracteres do diagnóstico de cada consulta.
 
SELECT diagnostico, SUBSTRING(diagnostico, 1, 5) AS cinco_primeiros
FROM Consulta;

-- Exercício 25 Mostre do segundo ao quinto caractere do nome de cada cliente.
SELECT nome, SUBSTRING(nome, 2, 4) AS segundo_ao_quinto
FROM Cliente;

-- Exercício 26 Mostre os três primeiros caracteres da cidade dos clientes.
SELECT cidade, SUBSTRING(cidade, 1, 3) AS tres_primeiros
FROM Cliente;

-- Exercício 27 Mostre o valor de cada consulta arredondado para zero casas decimais.
SELECT valor, ROUND(valor, 0) AS valor_arredondado
FROM Consulta;

-- Exercício 28 Mostre a média dos valores das consultas arredondada para duas casas decimais.
SELECT ROUND(AVG(valor), 2) AS media_arredondada
FROM Consulta;

-- Exercício 29 Mostre o valor de cada consulta arredondado para uma casa decimal.
SELECT valor, ROUND(valor, 1) AS valor_arredondado
FROM Consulta;

-- Exercício 30 Calcule o valor médio das consultas e apresente o resultado arredondado para zero casas decimais.
SELECT ROUND(AVG(valor), 0) AS media_arredondada
FROM Consulta;

-- Exercício 31 Mostre o nome de cada cliente em letras maiúsculas e a quantidade de caracteres do nome.
SELECT UPPER(nome) AS nome_maiusculo,
       LEN(nome) AS quantidade_caracteres
FROM Cliente;

-- Exercício 32 Mostre o nome do animal e os três primeiros caracteres do nome.
SELECT nome,
       SUBSTRING(nome, 1, 3) AS tres_primeiros
FROM Animal;

-- Exercício 33 Apresente o valor médio das consultas arredondado para duas casas decimais.
SELECT ROUND(AVG(valor), 2) AS valor_medio
FROM Consulta;

-- Exercício 34 Mostre a soma dos valores das consultas e o maior valor registrado.
SELECT SUM(valor) AS soma_valores,
       MAX(valor) AS maior_valor
FROM Consulta;

-- Exercício 35 Exiba o diagnóstico em letras maiúsculas e informe a quantidade de caracteres do texto.
SELECT UPPER(diagnostico) AS diagnostico_maiusculo,
       LEN(diagnostico) AS quantidade_caracteres
FROM Consulta;
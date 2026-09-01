use ClinicaVeterinaria

-- Exercício 1
SELECT COUNT(*) AS quantidade_clientes
FROM Cliente;

-- Exercício 2
SELECT COUNT(*) AS quantidade_animais
FROM Animal;

-- Exercício 3
SELECT COUNT(*) AS quantidade_consultas
FROM Consulta;

-- Exercício 4
SELECT SUM(valor) AS valor_total
FROM Consulta;

-- Exercício 5
SELECT AVG(valor) AS valor_medio
FROM Consulta;

-- Exercício 6
SELECT MAX(valor) AS maior_valor
FROM Consulta;

-- Exercício 7
SELECT MIN(valor) AS menor_valor
FROM Consulta;

-- Exercício 8
SELECT AVG(idade) AS idade_media
FROM Animal;

-- Exercício 9
SELECT MAX(idade) AS maior_idade
FROM Animal;

-- Exercício 10
SELECT MIN(idade) AS menor_idade
FROM Animal;

-- Exercício 11
SELECT nome, LEN(nome) AS quantidade_caracteres
FROM Cliente;

-- Exercício 12
SELECT nome, LEN(nome) AS quantidade_caracteres
FROM Animal;

-- Exercício 13
SELECT diagnostico, LEN(diagnostico) AS tamanho_texto
FROM Consulta;

-- Exercício 14
SELECT *
FROM Cliente
WHERE LEN(nome) > 10;

-- Exercício 15
SELECT *
FROM Animal
WHERE LEN(nome) = 5;

-- Exercício 16
SELECT UPPER(nome) AS nome_maiusculo
FROM Cliente;

-- Exercício 17
SELECT UPPER(nome) AS nome_maiusculo
FROM Animal;

-- Exercício 18
SELECT UPPER(diagnostico) AS diagnostico_maiusculo
FROM Consulta;

-- Exercício 19
SELECT LOWER(nome) AS nome_minusculo
FROM Cliente;

-- Exercício 20
SELECT LOWER(especie) AS especie_minuscula
FROM Animal;

-- Exercício 21
SELECT LOWER(raca) AS raca_minuscula
FROM Animal;

-- Exercício 22
SELECT nome, SUBSTRING(nome, 1, 3) AS tres_primeiros
FROM Cliente;

-- Exercício 23
SELECT nome, SUBSTRING(nome, 1, 4) AS quatro_primeiros
FROM Animal;

-- Exercício 24
SELECT diagnostico, SUBSTRING(diagnostico, 1, 5) AS cinco_primeiros
FROM Consulta;

-- Exercício 25
SELECT nome, SUBSTRING(nome, 2, 4) AS segundo_ao_quinto
FROM Cliente;

-- Exercício 26
SELECT cidade, SUBSTRING(cidade, 1, 3) AS tres_primeiros
FROM Cliente;

-- Exercício 27
SELECT valor, ROUND(valor, 0) AS valor_arredondado
FROM Consulta;

-- Exercício 28
SELECT ROUND(AVG(valor), 2) AS media_arredondada
FROM Consulta;

-- Exercício 29
SELECT valor, ROUND(valor, 1) AS valor_arredondado
FROM Consulta;

-- Exercício 30
SELECT ROUND(AVG(valor), 0) AS media_arredondada
FROM Consulta;

-- Exercício 31
SELECT UPPER(nome) AS nome_maiusculo,
       LEN(nome) AS quantidade_caracteres
FROM Cliente;

-- Exercício 32
SELECT nome,
       SUBSTRING(nome, 1, 3) AS tres_primeiros
FROM Animal;

-- Exercício 33
SELECT ROUND(AVG(valor), 2) AS valor_medio
FROM Consulta;

-- Exercício 34
SELECT SUM(valor) AS soma_valores,
       MAX(valor) AS maior_valor
FROM Consulta;

-- Exercício 35
SELECT UPPER(diagnostico) AS diagnostico_maiusculo,
       LEN(diagnostico) AS quantidade_caracteres
FROM Consulta;
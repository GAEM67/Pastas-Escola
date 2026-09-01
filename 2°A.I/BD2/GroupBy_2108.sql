-- Quantidade de clientes por cidade
SELECT cidade, COUNT(*) AS quantidade
FROM Cliente
GROUP BY cidade

-- Quantidade de animais por espécie
SELECT especie, COUNT(*)
FROM Animal
GROUP BY especie

-- Valor médio das consultas por animal
SELECT id_animal, AVG(valor) 
FROM Consulta
GROUP BY id_animal;

-- 1. Mostre o ID de cada cliente e a quantidade de animais que ele possui.
-- 2. Valor total das consultas por animal
-- 3. Valor médio das consultas por diagnóstico
-- 4. Quantidade de consultas por 

--Após explicação do having
-- 5. Mostre as espécies cujo valor médio das consultas seja maior que R$ 100,00.
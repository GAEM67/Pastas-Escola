create database Loja;
use Loja;

create table Cliente
(
  cod_clie numeric (4) primary key,
  nome_clie varchar(20) not null,
  endereco varchar (30),
  cidade varchar (15),
  cep char(8),
  uf char (2),
  cnpj char (16),
  ie char (12)
);
insert into Cliente values (720, 'Ana', 'Rua 17 n.19', 'Niterói', '24358310', 'RJ', '12113231/0001-34', '2134');
insert into Cliente values (870, 'Flavio', 'Av. Pres. Vargas, 10', 'São Paulo', '22763931', 'SP', '2276393/19387-9', '4631' );
insert into Cliente values (110, 'Jorge', 'Rua Caiapó, 13', 'Curitiba', '30078500', 'PR', '14512764/9834-9', null);
insert into Cliente values (222, 'Lúcia', 'Rua Itabira, 123', 'Belo Horizonte', '22124391', 'MG', '283152123/9348-8', '2985');
insert into Cliente values (830, 'Mauricio', 'Av. Paulista, 1236', 'São Paulo', '3012683', 'SP', '32816985/7465-6', '9343');
insert into Cliente values (130, 'Edmar', 'Rua da Praia, s/n', 'Salvador', '30079300', 'BA', '23463284/234-9', '7121');
insert into Cliente values (410, 'Rodolfo', 'Largo da Lapa, 27', 'Rio de Janeiro', '30078900', 'RJ', '12835128/2346-9', '7431');
insert into Cliente values (20, 'Beth', 'Av.Climério, 45', 'São Paulo', '25679300', 'SP', '32485126/7326-8', '9280');
insert into Cliente values (157, 'Paulo', 'Trav. Moraes, casa 3', 'Londrina', NULL, 'PR', '32848223/324-2', '1923');
insert into Cliente values (180 ,'Lívio', 'Av. Beira Mar, 1256','Florianópolis','30077500','SC','12736571/2347-4','1111');
insert into Cliente values (260, 'Susana', 'Rua Lopes Mendes, 12', 'Niterói', '30046500', 'RJ', '21763571/232-9', '2530');
insert into Cliente values (290, 'Renato', 'Rua Meireles, 123', 'São Paulo', '30225900', 'SP', '13276571/1231-4', NULL);
insert into Cliente values (390, 'Sebastião', 'Rua da Igreja, 10', 'Uberaba', '30438700', 'MG', '32176547/213-3', '1820');
insert into Cliente values (234, 'José', 'Quadra 3, Bl. 3, sl. 1003', 'Brasília', '22841650', 'DF', '21763576/1232-3', '2931');

create table Vendedor
(
cod_ven numeric (4) primary key,
nome_ven varchar (20) not null,
salario_fixo numeric (10,2),
comissao char (1),
);
insert into Vendedor values(209, 'José', 1800.00, 'C');
insert into Vendedor values(111, 'Carlos', 2490.00, 'A');
insert into Vendedor values(11, 'João', 2780.00, 'C');
insert into Vendedor values(240, 'Antônio', 9500.00, 'C');
insert into Vendedor values(720, 'Felipe', 4600.00, 'A');
insert into Vendedor values(213, 'Jonas', 2300.00, 'A');
insert into Vendedor values(101, 'João', 2650.00,'C');
insert into Vendedor values(310, 'Josias', 870.00, 'B');
insert into Vendedor values(250, 'Maurício',2930.00, 'B');

create table Produto
(
cod_prod numeric (4) primary key,
unidade varchar (3),
descricao varchar (20),
val_unit numeric (8,2),
);

insert into Produto values (25,'KG','Queijo',0,97);
insert into Produto values (31,'BAR','Chocolate',0,87);
insert into Produto values (78,'L','Vinho',2,00);
insert into Produto values (22,'M','Linho',0,11);
insert into Produto values (30,'SAC','Açúcar',0,30);
insert into Produto values (53,'M','Linha',1,80);
insert into Produto values (13,'G','Ouro',6,18);
insert into Produto values (45,'M','Madeira',0,25);
insert into Produto values (87,'M','Cano',1,97);
insert into Produto values (77,'M','Papel',1,05);



create table Pedido
(
num_pedido numeric (4) primary key,
pr_entrega numeric (3) not null,
cod_clie numeric (4) references Cliente (cod_clie),
cod_ven numeric (4) references Vendedor (cod_ven)
);

insert into Pedido values (121, 20, 410, 209);
insert into Pedido values (97, 20, 720, 101);
insert into Pedido values (101,15,720,101);
insert into Pedido values (137,20,720,720);
insert into Pedido values (148, 20, 720,101);
insert into Pedido values (189,15,870,213);
insert into Pedido values (104,30,110,101);
insert into Pedido values (203,30,830,250);
insert into Pedido values (98,20,410,209);
insert into Pedido values (143,30,20,111)
insert into Pedido values (105,30,180,240);
insert into Pedido values (111,15,260,240);
insert into Pedido values (103,20,260,11);
insert into Pedido values (91,20,260,11)
insert into Pedido values (138,20,260,11);
insert into Pedido values (108,15,290,310);
insert into Pedido values (119,30,390,250);
insert into Pedido values (127,10,410,11);




create table Item_Pedido
(
num_pedido numeric (4) references Pedido (num_pedido),
cod_prod numeric (4) references Produto (cod_prod),
quant numeric (8,2)
);

insert into Item_Pedido values(121, 25, 10);
insert into Item_Pedido values(121, 31, 35);
insert into Item_Pedido values(97, 77, 20);
insert into Item_Pedido values(101, 31, 9);
insert into Item_Pedido values(101, 78, 18);
insert into Item_Pedido values(101, 13, 5);
insert into Item_Pedido values(98, 77, 5);
insert into Item_Pedido values(148, 45, 8);
insert into Item_Pedido values(148, 77, 3);
insert into Item_Pedido values(148, 25, 10);
insert into Item_Pedido values(148, 78, 30);
insert into Item_Pedido values(104, 53, 32);
insert into Item_Pedido values(203, 31, 6);
insert into Item_Pedido values(189, 78, 45);
insert into Item_Pedido values(143, 31, 20);
insert into Item_Pedido values(143, 78, 10);




--SELECT campo FROM tabela
--Apelidar a coluna:
--EX:
--select nm_clie "Nome do cliente", from cliente
--Ordenar
--Sinstaxe: order by nome_col ou posição por número
--Asc - crescente
--Desc - decrescente
--Ex:
--select * from cliente ordey by nome_clie asc;
--select * from vendedor order by nome_ven desc;

--Ou por numero da coluna

--select * from vendedor order by 3 desc;
--select cidade, nome_clie from cliente order by 1, 2 desc;


-- Condições e filtros

-- Operadores - aritméticos + = * / ()
--EX:
--select nome_ven, salario_fixo "Salário atual", salario_fixo + 250 "Salário reajustado"
--from vendedor

-- Operadores Relacionais > >= < <= = <> ou !=
--select * fron vendedor where salario_fixo < 1500;

-- Operador lógicos and or not
--select * from vendedor where salario_fixo >= 1500 and salario_fixo < 3000;
--select * from vendedor where salario_fixo < 1500 or salario_fixo > 3000 order by 2;
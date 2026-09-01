create table aluno(
      rmm_numero numeric(6) primary key not null,
      nome varchar(40) not null,
      celular varchar(15)
);

insert into aluno( rmm_numero, nome) values (1, 'Gustavo')
insert into aluno values (2, 'Erick', '999999999999999')
insert into aluno (rmm_numero, celular, nome)
values(3, '99999999999', 'Gugu');

select * from aluno;

 -- update tabela set campo = valor;
 -- where 
 update aluno set celular = '123456789';

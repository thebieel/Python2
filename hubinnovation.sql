create database hub_innovation;
use hub_innovation;

create table usuario(
id_usuario int auto_increment primary key,
nome varchar(30) not null,
email varchar(30) not null,
telefone varchar(18)not null,
cpf varchar(20) not null,
data_nasc date not null,
sexo varchar (30) not null
);

create table palestra(
id_palestra int not null primary key,
desc_palestra text(200)not null,
nome_palestra varchar(40)not null,
vagas int not null,
id_palestrante int not null,
constraint foreign key (id_palestra) references usuario(id_usuario)
);
  
  

insert into usuario (nome,email,telefone,cpf,data_nasc,sexo)values
('Gabriel','gabpontes2005@gmail.com','67992778395','09837082456','2005-05-07','Masculino');


describe usuario;
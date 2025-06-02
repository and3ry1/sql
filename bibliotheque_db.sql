CREATE DATABASE IF NOT EXISTS custom_db;
USE custom_db;
CREATE TABLE IF NOT exists Employe (
id INT primary key,
Nom varchar(32),
age int check (Age >= 18)
);
show tables;

create table if  not exists Personne (
id int primary key auto_increment,
Titre varchar(10),
Prenom Varchar(50),
Nom Varchar(50),
Telephone varchar(20),
Email varchar(100)
);

create table  if not exists	 Adresse (
id INT primary key auto_increment,
personne_id int,
rue varchar(100),
ville varchar(50),
codepostal varchar(5),
foreign key (personne_id) references personne(id)
);

SELECT titre, nom, prenom  from personne where id > 1;

 
 


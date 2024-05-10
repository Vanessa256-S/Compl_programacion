CREATE DATABASE GRANJA
USE GRANJA
CREATE TABLE GANADO(
ID varchar(12) PRIMARY KEY,
Especie varchar(50)NOT NULL,
Raza varchar(50)NOT NULL,
Edad INT NOT NULL,
Peso INT NOT NULL,
ValorKilo INT NOT NULL,
Valortotal int NOT NULL,
);
CREATE TABLE Cultivos(
ID varchar(12) PRIMARY KEY,
Nombre varchar(50)NOT NULL,
Tipo varchar(50)NOT NULL,
Area INT NOT NULL,
Rendimiento INT NOT NULL,
ValorKilo INT NOT NULL,
Valortotal int NOT NULL,
);

select*from  GANADO;
select*from  Cultivos;


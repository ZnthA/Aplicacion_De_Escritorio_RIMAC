USE MASTER

create database RIMAC
GO


USE RIMAC
GO

CREATE TABLE RIMAC.DBO.usuarios
(  
   Id INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
   Usuario CHAR(8),
   Contrasena VARCHAR(8)
)
GO

INSERT INTO RIMAC.DBO.usuarios (Usuario, Contrasena) VALUES('12345678', '12345')
GO
INSERT INTO RIMAC.DBO.usuarios (Usuario, Contrasena) VALUES('76014559', '12345')
GO
INSERT INTO RIMAC.DBO.usuarios (Usuario, Contrasena) VALUES('admin', 'admin')
GO
SELECT * FROM RIMAC.DBO.usuarios
GO
SELECT @@version;

UPDATE usuarios
	SET Usuario = 'admin'
	where Id = 3
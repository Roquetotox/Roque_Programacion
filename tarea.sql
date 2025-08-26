CREATE TABLE Estudiantes1 (
    customer_id INT PRIMARY KEY,         
    nombre VARCHAR(100), 
    apellido VARCHAR(100),              
    edad INT,                           
    telefono VARCHAR(20)                
);
ALTER TABLE Estudiantes1
ADD COLUMN email VARCHAR(150);

INSERT INTO Estudiantes1 (customer_id, nombre, apellido, edad, telefono, email) VALUES
(1, 'Carlos', 'Bruzual', 28, 123456789, 'carlos.bruzual@email.com'),
(2, 'Jose', 'Colina', 34, 987654321, 'jose.colina@email.com'),
(3, 'Miguel', 'Colinas', 45, 654987, 'miguel.colinas@email.com'),
(4, 'Victor', 'Rodriguez', 22, 123456, 'victor.rodriguez@email.com'),
(5, 'Eliezer', 'Zambrano', 52, 987456, 'eliezer.zambrano@email.com'),
(6, 'Jean', 'Cefala', 22, 256489, 'jean.cefala@email.com'),
(7, 'Jaiver', 'Camacho', 28, 32659874, 'jaiver.camacho@email.com'),
(8, 'Diego', 'Hernandez', 21, 2563156, 'diego.hernandez@email.com'),
(9, 'Nestor', 'Nuñez', 29, 987466, 'nestor.nuñez@email.com'),
(10, 'Sebastian', 'Medina', 30,98746644, 'sebastian.medina@email.com'),
(11, 'Ezequiel', 'Garcia', 39, 5478952, 'ezequiel.garcia@email.com'),
(12, 'Roque', 'Oviedo', 16, 4859812, 'roque.oviedo@email.com');

SELECT nombre, apellido, telefono FROM Estudiantes1;
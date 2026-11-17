-- Creación de la tabla productos

create DATABASE inventario_db;

CREATE TABLE IF NOT EXISTS productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio NUMERIC(10, 2) NOT NULL
);

-- Datos de prueba opcionales
INSERT INTO productos (nombre, precio) VALUES
('Laptop Lenovo', 15500.00),
('Mouse Inalámbrico', 350.50),
('Teclado Mecánico', 1200.00),
('Monitor 24 Pulgadas', 3200.00);
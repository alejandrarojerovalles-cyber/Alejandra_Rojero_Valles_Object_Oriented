CREATE DATABASE IF NOT EXISTS login_system_db;
USE login_system_db;

CREATE TABLE IF NOT EXISTS users(
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(20) NOT NULL UNIQUE,
    password VARCHAR(256) NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Usuario de prueba predeterminado (Usuario: admin | Contraseña: admin123)
INSERT INTO users (username, password, nombre, email) 
VALUES ('admin', 'admin123', 'Administrador', 'admin@example.com');
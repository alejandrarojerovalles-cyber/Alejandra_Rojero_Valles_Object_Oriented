import psycopg2

class ProductoModel:
    def __init__(self):
        self.config = {
            "dbname": "inventario_db",
            "user": "postgres",
            "password": "0909",
            "host": "localhost",
            "port": "5432"
        }

    def obtener_conexion(self):
        return psycopg2.connect(**self.config)

    def obtener_todos(self):
        conexion = self.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT id, nombre, precio FROM productos ORDER BY id ASC;")
        registros = cursor.fetchall()
        cursor.close()
        conexion.close()
        return registros

    def insertar(self, nombre, precio):
        conexion = self.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO productos (nombre, precio) VALUES (%s, %s);", (nombre, precio))
        conexion.commit()
        cursor.close()
        conexion.close()
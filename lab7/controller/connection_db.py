import mysql.connector
from mysql.connector import Error
from controller.config import DB_config

class conexion_db:
    def __init__(self):
        self.config = DB_config

    def get_connection(self):
        try:
            conexion = mysql.connector.connect(**self.config)
            if conexion.is_connected():
                return conexion
        except Error as e:
            print(f"Error al conectar con MySQL: {e}")
            return None

    def ejecutar_consulta(self, query, params=()):
        conexion = self.get_connection() # Corregido para usar el nombre real del método
        if not conexion:
            return None
        
        cursor = conexion.cursor(dictionary=True)
        try:
            cursor.execute(query, params)
            
            # Si es una consulta SELECT, devolvemos los resultados
            if query.strip().upper().startswith("SELECT"):
                resultados = cursor.fetchall()
                return resultados
            else:
                # Si es INSERT, UPDATE o DELETE, guardamos los cambios
                conexion.commit()
                return cursor.rowcount
                
        except Error as e:
            print(f"Error en la consulta SQL: {e}")
            return None
        finally:
            if conexion and conexion.is_connected():
                cursor.close()
                conexion.close()
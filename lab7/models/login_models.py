from controller.connection_db import conexion_db

class User:
    def __init__(self, username, passw):
        self.username = username
        self.password = passw
        self.db = conexion_db()

    def auth(self):
        # Corregido 'passw' por 'password' para que coincida con la base de datos
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        result = self.db.ejecutar_consulta(query, (self.username, self.password))
        return result
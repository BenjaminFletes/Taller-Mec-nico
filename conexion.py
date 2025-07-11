import mysql.connector as Mysql

class conexion:

    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = ""
        self.database = "prueba"

    def open(self):
        self.conn = Mysql.connect(
            host=self.host, user=self.user,
            password=self.password, database=self.database
        )
        return self.conn
    
    def close(self):
        self.conn.close()

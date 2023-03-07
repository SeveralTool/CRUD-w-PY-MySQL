import mysql.connector
from mysql.connector import Error


class DAO():
    try:
        def _init_(self):
            self.conexion = mysql.connector.connect(
                host= "localhost",
                port= "3306",
                user= "root",
                password= "1234567",
                db= "testDB",
            )
    except Error as ex:
        print("Eroor al conectar con la DataBase:{0}".format(ex))
        
        
    def verUsers(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.curson()
                cursor.execute("SELECT * FROM users ORDER BY nombre ASC")
                resultado = cursor.fetchall()
                return resultado
            except Error as ex:
                print("Error al intentar la Query: {0}".format(ex))
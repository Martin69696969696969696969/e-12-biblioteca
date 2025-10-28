import mysql.connector
from mysql.connector import Error
import logging

logging.basicConfig(filename='biblioteca.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class ConexionBD:
    def __init__(self):
        self.conexion = None

    def conectar(self):
        try:
            self.conexion = mysql.connector.connect(
                host="localhost",
                user="root",
                password="toor",
                database="biblioteca",
                auth_plugin='mysql_native_password'
            )
            if self.conexion.is_connected():
                logging.info("Conexión establecida.")
                print("Conexión OK.")
        except Error as e:
            logging.error(f"Error conexión: {e}")
            print("Error: ", e)

    def ejecutar(self, query, params=None):
        cursor = self.conexion.cursor()
        try:
            cursor.execute(query, params)
            self.conexion.commit()
            return cursor
        except Error as e:
            self.conexion.rollback()
            logging.error(f"Error ejecutar: {e}")

    def consultar(self, query, params=None):
        cursor = self.conexion.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()

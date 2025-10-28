from conexion import ConexionBD
from modelos.usuario import Usuario
from modelos.libro import Libro
from modelos.prestamo import Prestamo

class Sistema:
    def __init__(self):
        self.db = ConexionBD()
        self.db.conectar()

    # CRUD USUARIOS
    def registrar_usuario(self):
        nombre = input("Nombre: ")
        tipo = input("Tipo (estudiante, profesor, admin): ")
        pwd = input("Contraseña: ")

        u = Usuario(nombre, tipo, pwd)
        self.db.ejecutar("INSERT INTO usuarios (nombre, tipo, password) VALUES (%s,%s,%s)",
                         u.datos_insert())
        print("Usuario registrado!")

    # CRUD LIBROS
    def registrar_libro(self):
        titulo = input("Título: ")
        autor = input("Autor: ")
        anio = int(input("Año: "))
        l = Libro(titulo, autor, anio)
        self.db.ejecutar("INSERT INTO libros (titulo, autor, anio, disponible) VALUES (%s,%s,%s,%s)",
                         l.datos_insert())
        print("Libro registrado!")

    def menu(self):
        while True:
            print("\n1. Usuarios 2. Libros 3. Salir")
            op = input("Opción: ")
            if op == "1":
                self.registrar_usuario()
            elif op == "2":
                self.registrar_libro()
            elif op == "3":
                break

if __name__ == "__main__":
    Sistema().menu()

import bcrypt

class Usuario:
    def __init__(self, nombre="", tipo="estudiante", password=""):
        self.__id = None
        self.__nombre = nombre
        self.__tipo = tipo
        self.__password = self.__encrypt(password)

    def __encrypt(self, pwd):
        if not pwd.strip():
            raise ValueError("Contraseña vacía")
        return bcrypt.hashpw(pwd.encode(), bcrypt.gensalt()).decode()

    def validar_password(self, pwd):
        return bcrypt.checkpw(pwd.encode(), self.__password.encode())

    def datos_insert(self):
        return (self.__nombre, self.__tipo, self.__password)

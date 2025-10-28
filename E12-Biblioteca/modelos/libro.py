class Libro:
    def __init__(self, titulo="", autor="", anio=0):
        self.__id = None
        self.__titulo = titulo
        self.__autor = autor
        self.__anio = anio
        self.__disp = True

    def datos_insert(self):
        return (self.__titulo, self.__autor, self.__anio, self.__disp)

from datetime import date

class Prestamo:
    def __init__(self, id_usuario, id_libro):
        self.id_usuario = id_usuario
        self.id_libro = id_libro
        self.fecha_prestamo = date.today()
        self.fecha_devolucion = None

    def datos_insert(self):
        return (self.id_usuario, self.id_libro, self.fecha_prestamo, self.fecha_devolucion)

class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre
        self.bienes_asignados = []

class Bien:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion


def asignar_bien(empleado, bien):
    empleado.bienes_asignados.append(bien)


def generar_reporte(empleado):
    print(f"Bienes asignados a {empleado.nombre}:")
    for bien in empleado.bienes_asignados:
        print(f"Nombre: {bien.nombre}, Descripción: {bien.descripcion}")



empleado1 = Empleado("Juan")
empleado2 = Empleado("María")


bien1 = Bien("Computadora", "Computadora de escritorio")
bien2 = Bien("Teléfono", "Teléfono móvil")


asignar_bien(empleado1, bien1)
asignar_bien(empleado2, bien2)

generar_reporte(empleado1)

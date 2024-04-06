class Bien:
    def __init__(self, placa, nombre, categoria, descripcion, estado):
        self.placa = placa
        self.nombre = nombre
        self.categoria = categoria
        self.descripcion = descripcion
        self.estado = estado
        self.asignado_a = None

class Empleado:
    def __init__(self, cedula, nombre, apellido, telefono, direccion, puesto, fecha_ingreso, es_jefe):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.direccion = direccion
        self.puesto = puesto
        self.fecha_ingreso = fecha_ingreso
        self.es_jefe = es_jefe

class AdministradorBienes:
    def __init__(self):
        self.bienes = []
        self.empleados = []

    def agregar_bien(self, bien):
        self.bienes.append(bien)
        print("Se agrega correctamente.")

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)
        print("Se agrega el empleado correctamente.")

    def mostrar_bienes(self):
        print("\nLista de Bienes:")
        for bien in self.bienes:
            asignado_a = "No asignado" if bien.asignado_a is None else f"Asignado a: {bien.asignado_a.nombre} {bien.asignado_a.apellido}"
            print(f"Placa: {bien.placa}, Nombre: {bien.nombre}, Categoría: {bien.categoria}, Descripción: {bien.descripcion}, Estado: {bien.estado}, {asignado_a}")

    def mostrar_empleados(self):
        print("\nLista de Empleados:")
        for empleado in self.empleados:
            print(f"Cédula: {empleado.cedula}, Nombre: {empleado.nombre}, Apellido: {empleado.apellido}, Teléfono: {empleado.telefono}, Dirección: {empleado.direccion}, Puesto: {empleado.puesto}, Fecha de ingreso: {empleado.fecha_ingreso}, Jefe: {'Sí' if empleado.es_jefe else 'No'}")

    def asignar_bien(self, placa, empleado):
        bien = self.buscar_bien(placa)
        if bien:
            if bien.estado == "Asignable":
                if bien.asignado_a is None:
                    bien.asignado_a = empleado
                    print(f"Bien {bien.placa} asignado correctamente a {empleado.nombre} {empleado.apellido}.")
                else:
                    print("El bien ya está asignado a otro empleado.")
            else:
                print("El estado del bien no es asignable.")
        else:
            print("No se encontró ningún bien con esa placa.")

    def buscar_bien(self, placa):
        for bien in self.bienes:
            if bien.placa == placa:
                return bien
        return None

# Función principal para interactuar con el usuario
def main():
    administrador = AdministradorBienes()

    empleado1 = Empleado("123456789", "Juan", "Pérez", "88956232", "San José", "Gerente", "01/01/2020", True)
    empleado2 = Empleado("987654321", "María", "González", "85764120", "San Joseé", "Asistente", "01/05/2021", False)
    administrador.agregar_empleado(empleado1)
    administrador.agregar_empleado(empleado2)

    placa = "AB-1234"
    nombre = "Computadora"
    categoria = "Electrónica"
    descripcion = "Computadora portátil"
    estado = "Asignable"
    bien = Bien(placa, nombre, categoria, descripcion, estado)
    administrador.agregar_bien(bien)

    placa = "CD-5678"
    nombre = "Impresora"
    categoria = "Oficina"
    descripcion = "Impresora láser"
    estado = "Asignable"
    bien = Bien(placa, nombre, categoria, descripcion, estado)
    administrador.agregar_bien(bien)

    administrador.mostrar_bienes()
    administrador.mostrar_empleados()

    # Asignar bien al empleado
    placa_asignar = input("Ingrese la placa del bien que desea asignar: ")
    empleado_asignar = input("Ingrese el nombre del empleado al que desea asignar el bien: ")
    empleado = next((emp for emp in administrador.empleados if emp.nombre == empleado_asignar), None)
    if empleado:
        administrador.asignar_bien(placa_asignar, empleado)
    else:
        print("No se encontró ningún empleado con ese nombre.")

if __name__ == "__main__":
    main()

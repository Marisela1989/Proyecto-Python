import pymongo

class Usuarios:
    def __init__(self, cedula, nombre, apellidos, telefono, direccion, puesto, fechaIngreso):
        self.cedula = cedula
        self.nombre = nombre
        self.apellidos = apellidos
        self.telefono = telefono
        self.direccion = direccion
        self.puesto = puesto
        self.fechaIngreso = fechaIngreso
        
    def guardar(self):
        estado=0
        usuario= pymongo.MongoClient("mongodb://localhost:27017")
        bd=usuario["empresa"]
        try:
            tbl=bd["usuario"]
            doc={"_id":self.cedula,
                "nombre":self.nombre,
                "apellidos":self.apellidos,
                "telefono":self.telefono,
                "direccion":self.direccion,
                "puesto":self.puesto,
                "fechaIngreso":self.fechaIngreso}
            tbl.insert_one(doc)
            estado=1
        except Exception:
            print("Error al guardar")
            estado=0 
        finally:
            usuario.close
            return estado
    
    def modificar(self):
        pass
    
    def eliminar(self):
        pass
    
    def getUsuarios(self):
        pass
            
    def getNumeroRegistros(self):
        pass     
import pymongo

class Empleados:
    def __init__(self, cedula=1, nombre=2, apellidos=3, telefono=4, direccion=5, puesto=6, fechaIngreso=7):
        self.cedula = cedula
        self.nombre = nombre
        self.apellidos = apellidos
        self.telefono = telefono
        self.direccion = direccion
        self.puesto = puesto
        self.fechaIngreso = fechaIngreso
        
    def guardar(self):
        estado = 0
        empleado = pymongo.MongoClient("mongodb://localhost:27017")
        bd = empleado["empresa"]
        try:
            tbl=bd["empleados"]
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
            empleado.close
        return estado
        
    def modificar(self):
        estado=0
        empleado= pymongo.MongoClient("mongodb://localhost:27017")
        bd=empleado["empresa"]
        try:
            tbl=bd["empleados"]
            #filtro
            filtro={"_id":self.cedula}
            
            doc = {
                "$set": {
                "nombre":self.nombre,
                "apellidos":self.apellidos,
                "telefono":self.telefono,
                "direccion":self.direccion,
                "puesto":self.puesto,
                "fechaIngreso":self.fechaIngreso,}
                }
            tbl.update_one(filtro,doc)
            estado=1
        except Exception:
            print("Error al modificar")
            estado=0 
        finally:
            empleado.close
        return estado
    
    def eliminar(self):
        estado=0
        empleado = pymongo.MongoClient("mongodb://localhost:27017")
        bd = empleado["empresa"]
        try:
            tbl=bd["empleados"]
            #filtro
            filtro={"_id":self.cedula}
            
            tbl.delete_one(filtro,doc)
            estado=1
        except Exception:
            print("Error al eliminar")
            estado=0 
        finally:
            empleado.close
        return estado
    
    def getEmpleados(self):
        empleado = pymongo.MongoClient("mongodb://localhost:27017")
        bd = empleado["empresa"]
        tbl=bd["empleados"]
        return tbl.find()
            
    def getNumeroRegistros(self):
        empleado = pymongo.MongoClient("mongodb://localhost:27017")
        bd = empleado["empresa"]
        size=bd.command("collstats","empleados")
        return size["count"]
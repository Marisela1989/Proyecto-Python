import pymongo

class Usuarios:
    def __init__(self, nombreCompleto, correoElectronico, genero, fechaNacimiento):
        self.nombreCompleto = nombreCompleto
        self.correoElectronico = correoElectronico
        self.genero = genero
        self.fechaNacimiento = fechaNacimiento
        
    def guardar(self):
        estado=0
        usuario= pymongo.MongoClient("mongodb://localhost:27017")
        bd=usuario["empresa"]
        try:
            if self.nombreCompleto.lower() == "administrador": 
                tbl=bd["usuarios"]
                doc={"_id":self.nombreCompleto,
                    "correoElectronico":self.correoElectronico,
                "genero":self.genero,
                "fechaNacimiento":self.fechaNacimiento}
            tbl.insert_one(doc)
            estado=1
        except Exception:
            print("No eres administrador")
            estado=0 
        finally:
            usuario.close
        return estado
        
    
    def modificar(self):
        estado=0
        usuario= pymongo.MongoClient("mongodb://localhost:27017")
        bd=usuario["empresa"]
        try:
            tbl=bd["usuario"]
            #filtro
            filtro={"_id":self.nombreCompleto}
            
            doc = {
                "$set": {
                "correoElectronico":self.correoElectronico,
                "genero":self.genero,
                "fechaNacimiento":self.fechaNacimiento}
                }
            tbl.insert_one(filtro,doc)
            estado=1
        except Exception:
            print("Error al modificar")
            estado=0 
        finally:
            usuario.close
        return estado
    
    def eliminar(self):
        pass
    
    def getUsuarios(self):
        pass
            
    def getNumeroRegistros(self):
        pass     
    def getEmpleados(self):
        pass
            
    def getNumeroRegistros(self):
        pass     
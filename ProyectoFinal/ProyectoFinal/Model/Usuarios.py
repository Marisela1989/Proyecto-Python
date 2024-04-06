import pymongo

class Usuarios:
    def __init__(self, usuario, contrasenia, jefatura):
        self.usuario = usuario
        self.contrasenia = contrasenia
        
    def guardar(self):
        estado = 0
        usuario = pymongo.MongoClient("mongodb://localhost:27017")
        bd = usuario["empresa"]
        try:
            tbl=bd["usuarios"]
            doc={"_id":self.usuario,
                    "nombre":self.contrasenia,}
            tbl.insert_one(doc)
            estado=1
        except Exception as e:
            print("Error al guardar:", e)
            estado=0 
        finally:
            usuario.close
        return estado
    
    def modificar(self):
        estado=0
        usuario= pymongo.MongoClient("mongodb://localhost:27017")
        bd=usuario["empresa"]
        try:
            tbl=bd["usuarios"]
            #filtro
            filtro={"_id":self.usuario}
            
            doc = {
                "$set": {
                "correoElectronico":self.contrasenia,
            }
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
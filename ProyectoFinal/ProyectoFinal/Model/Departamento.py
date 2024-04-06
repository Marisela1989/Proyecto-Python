import pymongo
class Departamentos:
    def __init__(self, codigo, nombreDepartamento):
        self.codigo = codigo
        self.nombreDepartamento = nombreDepartamento
        #self.jefatura = jefatura
        
    def guardar(self):
        estado = 0
        departamento = pymongo.MongoClient("mongodb://localhost:27017")
        bd = departamento["empresa"]
        try:
            tbl=bd["departamentos"]
            doc={"_id":self.codigo,
                    "codigo":self.nombreDepartamento}
            tbl.insert_one(doc)
            estado=1
        except Exception as e:
            print("Error al guardar:", e)
            estado=0 
        finally:
            departamento.close
        return estado    
    
    def modificar(self):
        estado=0
        departamento= pymongo.MongoClient("mongodb://localhost:27017")
        bd=departamento["empresa"]
        try:
            tbl=bd["departamentos"]
            #filtro
            filtro={"_id":self.codigo}
            doc = {
                "$set": {
                "nombreDepartamento":nombreDepartamento,
                }}
            tbl.update_one(filtro,doc)
            estado=1
        except Exception:
            print("Error al modificar")
            estado=0 
        finally:
            departamento.close
        return estado
    def eliminar(self):
        estado=0
        departamento = pymongo.MongoClient("mongodb://localhost:27017")
        bd =departamento["empresa"]
        try:
            tbl=bd["departamentos"]
            #filtro
            filtro={"_id":self.codigo}
            
            tbl.delete_one(filtro)
            estado=1
        except Exception:
            print("Error al eliminar")
            estado=0 
        finally:
            departamento.close
        return estado
    
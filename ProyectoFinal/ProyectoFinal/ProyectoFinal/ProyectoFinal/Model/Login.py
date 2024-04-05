import pymongo
class Login:
    def __init__(self, usuario, contrasenia):
        self.usuario = usuario
        self.contrasenia = contrasenia
        
    def validarLogin(self):
        if (usuario=="admin" and contrasenia== "1234"):
            return True
        else:
            return False        
    
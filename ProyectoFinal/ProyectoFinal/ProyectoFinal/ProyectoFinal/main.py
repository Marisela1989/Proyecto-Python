
from PyQt5.QtCore import Qt
import sys

#importar los widgets
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
#importar clases ui
from Ui_mdi import Ui_mdiWindow
from Ui_Usuario import Ui_Usuario
from Ui_empleado import Ui_Empleado
from Model.Usuario import Usuarios

class mdiApp(QMainWindow):
    #init al constructor
    def __init__(self):
        super().__init__()
        #instanciar la ventana
        self.uiMdi=Ui_mdiWindow()
        #generar los componentes
        self.uiMdi.setupUi(self)
        #estilos
        self.uiMdi.mdiArea.setFixedHeight(2000)
        self.uiMdi.mdiArea.setFixedWidth(2000)
        #definir los eventos
        self.initComponents()
        #mostrar la ventana
        self.show()

    def initComponents(self):
        self.uiMdi.mniUsuario.triggered.connect(self.openWinUsuario)
        self.uiMdi.mniEmpleado.triggered.connect(self.openWinEmpleado)
        
    def openWinUsuario(self):
        self.winUsuario=winUsuario()
        #agregar la ventana al mdi
        self.uiMdi.mdiArea.addSubWindow(self.winUsuario)
        #eventos
        self.winUsuario.uiUsuario.btnGuardar.clicked.connect(self.guardarUsuario)
        self.winUsuario.uiUsuario.btnModificar.clicked.connect(self.modificarUsuario)
        self.winUsuario.uiUsuario.btnEliminar.clicked.connect(self.eliminarUsuario)
        self.winUsuario.show()
        
    def msgBox(self,mensaje,icono,tipo=0):
        msg = QMessageBox()
        msg.setIcon(icono)
        msg.setText(mensaje)
        msg.setWindowTitle("Mensaje")
        retval=msg.exec()
        
    def guardarUsuario(self):
        usuario=Usuarios(self.winUsuario.uiUsuario.txtCedula.text(),
                        self.winUsuario.uiUsuario.txtNombre.text(),
                        self.winUsuario.uiUsuario.txtApellidos.text(),
                        self.winUsuario.uiUsuario.txtTelefono.text(),
                        self.winUsuario.uiUsuario.txtDireccion.text(),
                        self.winUsuario.uiUsuario.txtPuesto.text(),
                        self.winUsuario.uiUsuario.txtFechaIngreso.text())
        if usuario.guardar()==1:
            self.msgBox("Datos Guardados Correctamente",QMessageBox.Information)
        else:
            self.msgBox("Error al Guardar los Datos",QMessageBox.Warning)
        
    def modificarUsuario(self):
        self.msgBox("Datos Modificados Correctamente",QMessageBox.Information)  
    def eliminarUsuario(self):
        self.msgBox("Datos Eliminados Correctamente",QMessageBox.Information) 
        
    def openWinEmpleado(self):
        self.winEmpleado=winEmpleado()
        self.uiMdi.mdiArea.addSubWindow(self.winEmpleado)
        self.winEmpleado.show()
                
class winUsuario(QWidget):
    def __init__(self):
        super().__init__()
        self.uiUsuario=Ui_Usuario()
        self.uiUsuario.setupUi(self)
class winEmpleado(QWidget):
    def __init__(self):
        super().__init__()
        self.uiEmpleado=Ui_Empleado()
        self.uiEmpleado.setupUi(self)        
        
if __name__=="__main__":
    app=QApplication(sys.argv)
    #cargar ventana
    win=mdiApp()
    win.showMaximized()
    sys.exit(app.exec())
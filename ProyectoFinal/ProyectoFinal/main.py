
from PyQt5.QtCore import Qt
import sys

#importar los widgets
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
#importar clases ui
from Ui_mdi import Ui_mdiWindow
from Ui_Usuario import Ui_Usuario
from Ui_empleado import Ui_Empleado
from Ui_Departamento import Ui_Departamento
from Ui_Bienes import Ui_Bienes
from Model.Usuarios import Usuarios
from Model.Empleados import Empleados
from Model.Departamento import Departamentos


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
        self.uiMdi.mniDepartamento.triggered.connect(self.openWinDepartamento)
        self.uiMdi.mniBienes.triggered.connect(self.openWinBienes)
        
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
        self.msgBox("Datos del usuario correctos",QMessageBox.Information)
    def modificarUsuario(self):
        self.msgBox("Datos del usuario",QMessageBox.Information)  
    def eliminarUsuario(self):
        self.msgBox("Datos del usuario eliminados correctamente",QMessageBox.Information) 
        
    def openWinEmpleado(self):
        empleado=Empleados()
        self.winEmpleado=winEmpleado()
        self.uiMdi.mdiArea.addSubWindow(self.winEmpleado)
        self.winEmpleado.uiEmpleado.btnGuardar.clicked.connect(self.guardarEmpleado)
        self.winEmpleado.uiEmpleado.btnModificar.clicked.connect(self.modificarEmpleado)
        self.winEmpleado.uiEmpleado.btnEliminar.clicked.connect(self.eliminarEmpleado)
        self.winEmpleado.uiEmpleado.btnCancelar.clicked.connect(self.limpiar)
        self.winEmpleado.uiEmpleado.tableWidget.clicked.connect(self.cargarDatos)
        self.cargarTabla(empleado.getNumeroRegistros(),empleado.getEmpleados())
        self.habilitarGuardar()
        self.winEmpleado.show()
        
    def guardarEmpleado(self):
        empleado=Empleados(self.winEmpleado.uiEmpleado.txtCedula.text(),
                        self.winEmpleado.uiEmpleado.txtNombre.text(),
                        self.winEmpleado.uiEmpleado.txtApellidos.text(),
                        self.winEmpleado.uiEmpleado.txtTelefono.text(),
                        self.winEmpleado.uiEmpleado.txtDireccion.text(),
                        self.winEmpleado.uiEmpleado.txtPuesto.text(),
                        self.winEmpleado.uiEmpleado.txtFechaIngreso.text()
                        )
        if empleado.guardar() == 1:
            self.msgBox("Datos del empleado guardados correctamente", QMessageBox.Information)
            self.limpiar()
            self.cargarTabla(empleado.getNumeroRegistros(),empleado.getEmpleados())
        else:
            self.msgBox("Error al guardar los datos del empleado", QMessageBox.Warning)
            
    def modificarEmpleado(self):
        empleado=Empleados(self.winEmpleado.uiEmpleado.txtCedula.text(),
                        self.winEmpleado.uiEmpleado.txtNombre.text(),
                        self.winEmpleado.uiEmpleado.txtApellidos.text(),
                        self.winEmpleado.uiEmpleado.txtTelefono.text(),
                        self.winEmpleado.uiEmpleado.txtDireccion.text(),
                        self.winEmpleado.uiEmpleado.txtPuesto.text(),
                        self.winEmpleado.uiEmpleado.txtFechaIngreso.text()
                        )
        if empleado.modificar() == 1:
            self.msgBox("Datos del empleado modificados correctamente" , QMessageBox.Information)
            self.limpiar()
            self.cargarTabla(empleado.getNumeroRegistros(),empleado.getEmpleados())
        else:
            self.msgBox("Error al modificar los datos del empleado", QMessageBox.Warning) 
            
    def eliminarEmpleado(self):
        empleado=Empleados(self.winEmpleado.uiEmpleado.txtCedula.text(),
                        self.winEmpleado.uiEmpleado.txtNombre.text(),
                        self.winEmpleado.uiEmpleado.txtApellidos.text(),
                        self.winEmpleado.uiEmpleado.txtTelefono.text(),
                        self.winEmpleado.uiEmpleado.txtDireccion.text(),
                        self.winEmpleado.uiEmpleado.txtPuesto.text(),
                        self.winEmpleado.uiEmpleado.txtFechaIngreso.text()
                        )
        if empleado.eliminar() == 1:
            self.msgBox("Datos del empleado eliminados correctamente", QMessageBox.Information)
            self.limpiar()
            self.cargarTabla(empleado.getNumeroRegistros(),empleado.getEmpleados())
        else:
            self.msgBox("Error al eliminar los datos del empleado", QMessageBox.Warning) 
        
    def cargarTabla(self,numFilas,datos):
        #determinar el # de filas de la tabla
        self.winEmpleado.uiEmpleado.tableWidget.setRowCount(numFilas)
        #determinar el numero de columnas
        self.winEmpleado.uiEmpleado.tableWidget.setColumnCount(7)
        i=0 
        for d in datos:
            print(d)
            self.winEmpleado.uiEmpleado.tableWidget.setItem(i,0,QTableWidgetItem(d["_id"]))
            self.winEmpleado.uiEmpleado.tableWidget.setItem(i,1,QTableWidgetItem(d["nombre"]))
            self.winEmpleado.uiEmpleado.tableWidget.setItem(i,2,QTableWidgetItem(d["apellidos"]))
            self.winEmpleado.uiEmpleado.tableWidget.setItem(i,3,QTableWidgetItem(d["telefono"]))
            self.winEmpleado.uiEmpleado.tableWidget.setItem(i,4,QTableWidgetItem(d["direccion"]))
            self.winEmpleado.uiEmpleado.tableWidget.setItem(i,5,QTableWidgetItem(d["puesto"]))
            self.winEmpleado.uiEmpleado.tableWidget.setItem(i,6,QTableWidgetItem(d["fechaIngreso"]))
            i+=1
    
    def cargarDatos(self):
        self.habilitarModificarEliminar()
        numFilas=self.winEmpleado.uiEmpleado.tableWidget.currentRow()
        self.winEmpleado.uiEmpleado.txtCedula.setText(self.winEmpleado.uiEmpleado.tableWidget.item(numFilas,0).text())
        self.winEmpleado.uiEmpleado.txtNombre.setText(self.winEmpleado.uiEmpleado.tableWidget.item(numFilas,1).text())
        self.winEmpleado.uiEmpleado.txtApellidos.setText(self.winEmpleado.uiEmpleado.tableWidget.item(numFilas,2).text())
        self.winEmpleado.uiEmpleado.txtTelefono.setText(self.winEmpleado.uiEmpleado.tableWidget.item(numFilas,3).text())
        self.winEmpleado.uiEmpleado.txtDireccion.setText(self.winEmpleado.uiEmpleado.tableWidget.item(numFilas,4).text())
        self.winEmpleado.uiEmpleado.txtPuesto.setText(self.winEmpleado.uiEmpleado.tableWidget.item(numFilas,5).text())
        self.winEmpleado.uiEmpleado.txtFechaIngreso.setText(self.winEmpleado.uiEmpleado.tableWidget.item(numFilas,6).text())
        
    def habilitarGuardar(self):
        self.winEmpleado.uiEmpleado.btnGuardar.setEnabled(True)
        self.winEmpleado.uiEmpleado.btnModificar.setEnabled(False)
        self.winEmpleado.uiEmpleado.btnEliminar.setEnabled(False)    
        
    def habilitarModificarEliminar(self):
        self.winEmpleado.uiEmpleado.btnGuardar.setEnabled(False)
        self.winEmpleado.uiEmpleado.btnModificar.setEnabled(True)
        self.winEmpleado.uiEmpleado.btnEliminar.setEnabled(True) 
        
    def limpiar(self):
        self.winEmpleado.uiEmpleado.txtCedula.setText("")
        self.winEmpleado.uiEmpleado.txtNombre.setText("")
        self.winEmpleado.uiEmpleado.txtApellidos.setText("")
        self.winEmpleado.uiEmpleado.txtTelefono.setText("")
        self.winEmpleado.uiEmpleado.txtDireccion.setText("")
        self.winEmpleado.uiEmpleado.txtPuesto.setText("")
        self.winEmpleado.uiEmpleado.txtFechaIngreso.setText("")     
        self.habilitarGuardar()   
        
    def openWinDepartamento(self):
        self.winDepartamento=winDepartamento()
        #agregar la ventana al mdi
        self.uiMdi.mdiArea.addSubWindow(self.winDepartamento)
        #eventos
        self.winDepartamento.uiDepartamento.btnGuardar.clicked.connect(self.guardarDepartamento)
        self.winDepartamento.uiDepartamento.btnModificar.clicked.connect(self.modificarDepartamento)
        self.winDepartamento.uiDepartamento.btnEliminar.clicked.connect(self.eliminarDepartamento)
        self.winDepartamento.show()        
        
    def guardarDepartamento(self):
        departamento=Departamentos(self.winDepartamento.uiDepartamento.txtCodigo.text(),
                                self.winDepartamento.uiDepartamento.txtNombreDepartamento.text()
                                )
        if departamento.guardar() == 1:
            self.msgBox("Datos del departamento guardados correctamente", QMessageBox.Information)
        else:
            self.msgBox("Error al guardar los datos del departamento", QMessageBox.Warning)
            
    def modificarDepartamento(self):
        departamento=Departamentos(self.winDepartamento.uiDepartamento.txtCodigo.text(),
                                self.winDepartamento.uiDepartamento.txtNombreDepartamento.text()
                                )
        if departamento.modificar() == 1:
            self.msgBox("Datos del departamento modificados correctamente", QMessageBox.Information)
        else:
            self.msgBox("Error al modificar los datos del departamento", QMessageBox.Warning)
            
    def eliminarDepartamento(self):
        departamento=Departamentos(self.winDepartamento.uiDepartamento.txtCodigo.text(),
                                self.winDepartamento.uiDepartamento.txtNombreDepartamento.text()
                                )
        if departamento.eliminar() == 1:
            self.msgBox("Datos del departamento eliminados correctamente", QMessageBox.Information)
        else:
            self.msgBox("Error al eliminar los datos del departamento", QMessageBox.Warning)    
        
    def openWinAsignacion(self):
        self.winAsignacion=winAsignacion()
        #agregar la ventana al mdi
        self.uiMdi.mdiArea.addSubWindow(self.winAsignacion)
        #eventos
        self.winAsignacion.show()   
        
    def openWinBienes(self):
        self.winBienes=winBienes()
        #agregar la ventana al mdi
        self.uiMdi.mdiArea.addSubWindow(self.winBienes)
        #eventos
        self.winBienes.show()   
            
            

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

class winDepartamento(QWidget):
    def __init__(self):
        super().__init__()
        self.uiDepartamento=Ui_Departamento()
        self.uiDepartamento.setupUi(self)           
        
class winAsignacion(QWidget):
    def __init__(self):
        super().__init__()
        self.uiAsignacion=Ui_AsignacionBienes()
        self.uiAsignacion.setupUi(self) 
        
class winBienes(QWidget):
    def __init__(self):
        super().__init__()
        self.uiBienes=Ui_Bienes()
        self.uiBienes.setupUi(self)        
        
        
if __name__=="__main__":
    app=QApplication(sys.argv)
    #cargar ventana
    win=mdiApp()
    win.showMaximized()
    sys.exit(app.exec())

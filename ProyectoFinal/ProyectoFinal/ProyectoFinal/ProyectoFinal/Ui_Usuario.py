# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\HP\OneDrive - Universidad Internacional de las Américas (UIA)\Escritorio\Proyecto-Python\ProyectoFinal\ProyectoFinal\ProyectoFinal\ProyectoFinal\Usuario.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Usuario(object):
    def setupUi(self, Usuario):
        Usuario.setObjectName("Usuario")
        Usuario.resize(800, 800)
        Usuario.setMinimumSize(QtCore.QSize(800, 800))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\HP\\OneDrive - Universidad Internacional de las Américas (UIA)\\Escritorio\\Proyecto-Python\\ProyectoFinal\\ProyectoFinal\\ProyectoFinal\\ProyectoFinal\\recursos/trespatitos.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Usuario.setWindowIcon(icon)
        self.formLayoutWidget = QtWidgets.QWidget(Usuario)
        self.formLayoutWidget.setGeometry(QtCore.QRect(200, 200, 391, 221))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.lblUsuario = QtWidgets.QLabel(self.formLayoutWidget)
        self.lblUsuario.setObjectName("lblUsuario")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblUsuario)
        self.txtUsuario = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtUsuario.setObjectName("txtUsuario")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtUsuario)
        self.lblContrasenia = QtWidgets.QLabel(self.formLayoutWidget)
        self.lblContrasenia.setObjectName("lblContrasenia")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblContrasenia)
        self.txtContrasenia = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtContrasenia.setObjectName("txtContrasenia")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtContrasenia)
        self.comboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setItemText(1, "")
        self.comboBox.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.lblRol = QtWidgets.QLabel(self.formLayoutWidget)
        self.lblRol.setObjectName("lblRol")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lblRol)
        self.lblTitulo = QtWidgets.QLabel(Usuario)
        self.lblTitulo.setGeometry(QtCore.QRect(360, 70, 121, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lblTitulo.setFont(font)
        self.lblTitulo.setObjectName("lblTitulo")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Usuario)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(160, 420, 471, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnGuardar = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnGuardar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\HP\\OneDrive - Universidad Internacional de las Américas (UIA)\\Escritorio\\Proyecto-Python\\ProyectoFinal\\ProyectoFinal\\ProyectoFinal\\ProyectoFinal\\recursos/save.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnGuardar.setIcon(icon1)
        self.btnGuardar.setObjectName("btnGuardar")
        self.horizontalLayout.addWidget(self.btnGuardar)
        self.btnModificar = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnModificar.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("c:\\Users\\HP\\OneDrive - Universidad Internacional de las Américas (UIA)\\Escritorio\\Proyecto-Python\\ProyectoFinal\\ProyectoFinal\\ProyectoFinal\\ProyectoFinal\\recursos/editar.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnModificar.setIcon(icon2)
        self.btnModificar.setObjectName("btnModificar")
        self.horizontalLayout.addWidget(self.btnModificar)
        self.btnEliminar = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnEliminar.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("c:\\Users\\HP\\OneDrive - Universidad Internacional de las Américas (UIA)\\Escritorio\\Proyecto-Python\\ProyectoFinal\\ProyectoFinal\\ProyectoFinal\\ProyectoFinal\\recursos/delete.webp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEliminar.setIcon(icon3)
        self.btnEliminar.setObjectName("btnEliminar")
        self.horizontalLayout.addWidget(self.btnEliminar)
        self.btnCancelar = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnCancelar.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("c:\\Users\\HP\\OneDrive - Universidad Internacional de las Américas (UIA)\\Escritorio\\Proyecto-Python\\ProyectoFinal\\ProyectoFinal\\ProyectoFinal\\ProyectoFinal\\recursos/salir.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCancelar.setIcon(icon4)
        self.btnCancelar.setObjectName("btnCancelar")
        self.horizontalLayout.addWidget(self.btnCancelar)
        self.lblImagen = QtWidgets.QLabel(Usuario)
        self.lblImagen.setGeometry(QtCore.QRect(620, 70, 141, 131))
        self.lblImagen.setText("")
        self.lblImagen.setPixmap(QtGui.QPixmap("c:\\Users\\HP\\OneDrive - Universidad Internacional de las Américas (UIA)\\Escritorio\\Proyecto-Python\\ProyectoFinal\\ProyectoFinal\\ProyectoFinal\\ProyectoFinal\\recursos/avatar.jpeg"))
        self.lblImagen.setScaledContents(True)
        self.lblImagen.setObjectName("lblImagen")
        self.tableWidget = QtWidgets.QTableWidget(Usuario)
        self.tableWidget.setGeometry(QtCore.QRect(10, 520, 781, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.retranslateUi(Usuario)
        QtCore.QMetaObject.connectSlotsByName(Usuario)

    def retranslateUi(self, Usuario):
        _translate = QtCore.QCoreApplication.translate
        Usuario.setWindowTitle(_translate("Usuario", "Usuario"))
        self.lblUsuario.setText(_translate("Usuario", "Usuario:"))
        self.lblContrasenia.setText(_translate("Usuario", "Contraseña:"))
        self.comboBox.setItemText(0, _translate("Usuario", "Administrador"))
        self.comboBox.setItemText(2, _translate("Usuario", "Empleado"))
        self.lblRol.setText(_translate("Usuario", "Rol:"))
        self.lblTitulo.setText(_translate("Usuario", "Usuario"))

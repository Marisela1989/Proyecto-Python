# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\HP\OneDrive - Universidad Internacional de las Américas (UIA)\Escritorio\Proyecto-Python\ProyectoFinal\ProyectoFinal\ProyectoFinal\ProyectoFinal\Bienes.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Bienes(object):
    def setupUi(self, Bienes):
        Bienes.setObjectName("Bienes")
        Bienes.resize(1000, 800)
        Bienes.setMinimumSize(QtCore.QSize(1000, 800))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\HP\\OneDrive - Universidad Internacional de las Américas (UIA)\\Escritorio\\Proyecto-Python\\ProyectoFinal\\ProyectoFinal\\ProyectoFinal\\ProyectoFinal\\recursos/trespatitos.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Bienes.setWindowIcon(icon)
        self.lblTitulo = QtWidgets.QLabel(Bienes)
        self.lblTitulo.setGeometry(QtCore.QRect(340, 60, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lblTitulo.setFont(font)
        self.lblTitulo.setObjectName("lblTitulo")
        self.formLayoutWidget = QtWidgets.QWidget(Bienes)
        self.formLayoutWidget.setGeometry(QtCore.QRect(290, 110, 401, 141))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.lblPlaca = QtWidgets.QLabel(self.formLayoutWidget)
        self.lblPlaca.setObjectName("lblPlaca")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblPlaca)
        self.lblNombre = QtWidgets.QLabel(self.formLayoutWidget)
        self.lblNombre.setObjectName("lblNombre")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblNombre)
        self.lblCategoria = QtWidgets.QLabel(self.formLayoutWidget)
        self.lblCategoria.setObjectName("lblCategoria")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lblCategoria)
        self.lblDescirpcion = QtWidgets.QLabel(self.formLayoutWidget)
        self.lblDescirpcion.setObjectName("lblDescirpcion")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lblDescirpcion)
        self.txtPlaca = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtPlaca.setObjectName("txtPlaca")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtPlaca)
        self.txtNombre = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtNombre.setObjectName("txtNombre")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtNombre)
        self.txtCategoria = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtCategoria.setObjectName("txtCategoria")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txtCategoria)
        self.txtDescripcion = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtDescripcion.setObjectName("txtDescripcion")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txtDescripcion)
        self.lblImagen = QtWidgets.QLabel(Bienes)
        self.lblImagen.setGeometry(QtCore.QRect(790, 100, 151, 121))
        self.lblImagen.setText("")
        self.lblImagen.setPixmap(QtGui.QPixmap("c:\\Users\\HP\\OneDrive - Universidad Internacional de las Américas (UIA)\\Escritorio\\Proyecto-Python\\ProyectoFinal\\ProyectoFinal\\ProyectoFinal\\ProyectoFinal\\recursos/imagen.png"))
        self.lblImagen.setScaledContents(True)
        self.lblImagen.setObjectName("lblImagen")
        self.comboBox = QtWidgets.QComboBox(Bienes)
        self.comboBox.setGeometry(QtCore.QRect(390, 280, 171, 31))
        self.comboBox.setStyleSheet("")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Bienes)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(180, 340, 641, 80))
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
        self.tableWidget = QtWidgets.QTableWidget(Bienes)
        self.tableWidget.setGeometry(QtCore.QRect(15, 441, 961, 291))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.retranslateUi(Bienes)
        QtCore.QMetaObject.connectSlotsByName(Bienes)

    def retranslateUi(self, Bienes):
        _translate = QtCore.QCoreApplication.translate
        Bienes.setWindowTitle(_translate("Bienes", "Bienes"))
        self.lblTitulo.setText(_translate("Bienes", "Información de Bienes"))
        self.lblPlaca.setText(_translate("Bienes", "Placa:"))
        self.lblNombre.setText(_translate("Bienes", "Nombre:"))
        self.lblCategoria.setText(_translate("Bienes", "Categoría:"))
        self.lblDescirpcion.setText(_translate("Bienes", "Descripción:"))
        self.comboBox.setItemText(0, _translate("Bienes", "Estado del Bien."))
        self.comboBox.setItemText(1, _translate("Bienes", "Asignable."))
        self.comboBox.setItemText(2, _translate("Bienes", "Exclusión."))
        self.comboBox.setItemText(3, _translate("Bienes", "Reparación."))

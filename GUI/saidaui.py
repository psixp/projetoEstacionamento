# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'saida.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Saida(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(223, 200)
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 10, 201, 181))
        self.groupBox_3.setObjectName("groupBox_3")
        self.placa = QtWidgets.QLabel(self.groupBox_3)
        self.placa.setGeometry(QtCore.QRect(10, 20, 61, 16))
        self.placa.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.placa.setObjectName("placa")
        self.box = QtWidgets.QLabel(self.groupBox_3)
        self.box.setGeometry(QtCore.QRect(10, 40, 61, 16))
        self.box.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.box.setObjectName("box")
        self.hrSaida = QtWidgets.QLabel(self.groupBox_3)
        self.hrSaida.setGeometry(QtCore.QRect(10, 80, 61, 16))
        self.hrSaida.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.hrSaida.setObjectName("hrSaida")
        self.dtEntrada = QtWidgets.QLabel(self.groupBox_3)
        self.dtEntrada.setGeometry(QtCore.QRect(10, 60, 61, 16))
        self.dtEntrada.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.dtEntrada.setObjectName("dtEntrada")
        self.dtSaida = QtWidgets.QLabel(self.groupBox_3)
        self.dtSaida.setGeometry(QtCore.QRect(10, 100, 61, 16))
        self.dtSaida.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.dtSaida.setObjectName("dtSaida")
        self.hrEntrada = QtWidgets.QLabel(self.groupBox_3)
        self.hrEntrada.setGeometry(QtCore.QRect(10, 120, 61, 16))
        self.hrEntrada.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.hrEntrada.setObjectName("hrEntrada")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_7.setGeometry(QtCore.QRect(80, 20, 113, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_8.setGeometry(QtCore.QRect(80, 40, 113, 20))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_9.setGeometry(QtCore.QRect(80, 60, 113, 20))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_10.setGeometry(QtCore.QRect(80, 80, 113, 20))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_11.setGeometry(QtCore.QRect(80, 100, 113, 20))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.buttonBox_2 = QtWidgets.QDialogButtonBox(self.groupBox_3)
        self.buttonBox_2.setGeometry(QtCore.QRect(20, 150, 156, 23))
        self.buttonBox_2.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox_2.setObjectName("buttonBox_2")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_12.setGeometry(QtCore.QRect(80, 120, 113, 20))
        self.lineEdit_12.setObjectName("lineEdit_12")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Registro de Entrada"))
        self.groupBox_3.setTitle(_translate("Form", "Saída"))
        self.placa.setText(_translate("Form", "Placa"))
        self.box.setText(_translate("Form", "Nº do Box"))
        self.hrSaida.setText(_translate("Form", "H. Saída"))
        self.dtEntrada.setText(_translate("Form", "D. Entrada"))
        self.dtSaida.setText(_translate("Form", "D. Saída"))
        self.hrEntrada.setText(_translate("Form", "H. Entrada"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Saida()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

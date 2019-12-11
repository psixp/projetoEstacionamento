# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'saida.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Saida(object):
    def setupUi(self, Form2Saida):
        Form2Saida.setObjectName("Form2Saida")
        Form2Saida.resize(223, 200)
        self.groupBox_3 = QtWidgets.QGroupBox(Form2Saida)
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
        self.saidaplaca = QtWidgets.QLineEdit(self.groupBox_3)
        self.saidaplaca.setGeometry(QtCore.QRect(80, 20, 113, 20))
        self.saidaplaca.setObjectName("saidaplaca")
        self.saidaplaca.setText("importar do banco")
        self.boxsaida = QtWidgets.QLineEdit(self.groupBox_3)
        self.boxsaida.setGeometry(QtCore.QRect(80, 40, 113, 20))
        self.boxsaida.setObjectName("boxsaida")
        self.boxsaida.setText("importar do banco 2")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_9.setGeometry(QtCore.QRect(80, 60, 113, 20))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_9.setText("importar do banco 3")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_10.setGeometry(QtCore.QRect(80, 80, 113, 20))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_10.setText("importar do banco 4")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_11.setGeometry(QtCore.QRect(80, 100, 113, 20))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_11.setText("importar do banco 5")
        self.buttonBox_2 = QtWidgets.QDialogButtonBox(self.groupBox_3)
        self.buttonBox_2.setGeometry(QtCore.QRect(20, 150, 156, 23))
        self.buttonBox_2.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox_2.setObjectName("buttonBox_2")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_12.setGeometry(QtCore.QRect(80, 120, 113, 20))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_12.setText("importar do banco 6")

        self.retranslateUi(Form2Saida)
        QtCore.QMetaObject.connectSlotsByName(Form2Saida)

    def retranslateUi(self, Form2Saida):
        _translate = QtCore.QCoreApplication.translate
        Form2Saida.setWindowTitle(_translate("Form", "Registro de Entrada"))
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
    Form2Saida = QtWidgets.QWidget()
    ui = Ui_Saida()
    ui.setupUi(Form2Saida)
    Form2Saida.show()
    sys.exit(app.exec_())

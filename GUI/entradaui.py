# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'entrada.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from geraPlaca import placa_gen, box_gen, hm_gen, dt_gen
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Entrada(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(224, 199)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 201, 181))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_81 = QtWidgets.QLabel(self.groupBox_2)
        self.label_81.setGeometry(QtCore.QRect(10, 20, 61, 16))
        self.label_81.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_81.setObjectName("label_81")
        self.label_82 = QtWidgets.QLabel(self.groupBox_2)
        self.label_82.setGeometry(QtCore.QRect(10, 40, 61, 16))
        self.label_82.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_82.setObjectName("label_82")
        self.label_83 = QtWidgets.QLabel(self.groupBox_2)
        self.label_83.setGeometry(QtCore.QRect(10, 80, 61, 16))
        self.label_83.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_83.setObjectName("label_83")
        self.label_84 = QtWidgets.QLabel(self.groupBox_2)
        self.label_84.setGeometry(QtCore.QRect(10, 60, 61, 16))
        self.label_84.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_84.setObjectName("label_84")
        self.label_85 = QtWidgets.QLabel(self.groupBox_2)
        self.label_85.setGeometry(QtCore.QRect(10, 100, 61, 16))
        self.label_85.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_85.setObjectName("label_85")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit.setGeometry(QtCore.QRect(80, 20, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText(placa_gen()) ######### JÁ VEM COM A PLACA PREENCHIDA ####################
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 40, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setText(box_gen()) ######### JÁ VEM COM A BOX PREENCHIDA ####################
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(80, 60, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setText(dt_gen())
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(80, 80, 113, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(80, 100, 113, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.groupBox_2)
        self.buttonBox.setGeometry(QtCore.QRect(20, 150, 156, 23))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_86 = QtWidgets.QLabel(self.groupBox_2)
        self.label_86.setGeometry(QtCore.QRect(10, 120, 61, 16))
        self.label_86.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_86.setObjectName("label_86")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(80, 120, 113, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.setText(hm_gen()) ######### JÁ VEM COM A HORA DE ENTRADA PREENCHIDA ####################

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Registro de Saída"))
        self.groupBox_2.setTitle(_translate("Form", "Entrada"))
        self.label_81.setText(_translate("Form", "Placa"))
        self.label_82.setText(_translate("Form", "Nº do Box"))
        self.label_83.setText(_translate("Form", "H. Saída"))
        self.label_84.setText(_translate("Form", "D. Entrada"))
        self.label_85.setText(_translate("Form", "D. Saída"))
        self.label_86.setText(_translate("Form", "H. Entrada"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Entrada()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

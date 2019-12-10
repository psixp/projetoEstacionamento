# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'entrada.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from geraPlaca import placa_gen, box_gen, hm_gen, dt_gen
from PyQt5 import QtCore, QtGui, QtWidgets
from clientes import Placas
import sqlite3

class Ui_Entrada(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(224, 199)



        self.itensDicio = None
        self.btAcpOrRejct = False
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 201, 181))
        self.groupBox_2.setObjectName("groupBox_2")
        self.Placa = QtWidgets.QLabel(self.groupBox_2)
        self.Placa.setGeometry(QtCore.QRect(10, 20, 61, 16))
        self.Placa.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.Placa.setObjectName("PLACA")
        self.Box = QtWidgets.QLabel(self.groupBox_2)
        self.Box.setGeometry(QtCore.QRect(10, 40, 61, 16))
        self.Box.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.Box.setObjectName("BOX")
        self.DtEntrada = QtWidgets.QLabel(self.groupBox_2)
        self.DtEntrada.setGeometry(QtCore.QRect(10, 60, 61, 16))
        self.DtEntrada.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.DtEntrada.setObjectName("D. Entrada")
        self.HrEntrada = QtWidgets.QLabel(self.groupBox_2)
        self.HrEntrada.setGeometry(QtCore.QRect(10, 80, 61, 16))
        self.HrEntrada.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.HrEntrada.setObjectName("H. Entrada")
        self.getPlaca = QtWidgets.QLineEdit(self.groupBox_2)
        self.getPlaca.setGeometry(QtCore.QRect(80, 20, 113, 20))
        self.getPlaca.setObjectName("PLACA")
        self.getPlaca.setText(placa_gen()) ######### JÁ VEM COM A PLACA PREENCHIDA ####################
        self.getBox = QtWidgets.QLineEdit(self.groupBox_2)
        self.getBox.setGeometry(QtCore.QRect(80, 40, 113, 20))
        self.getBox.setObjectName("BOX")
        self.getBox.setText(box_gen()) ######### JÁ VEM COM A BOX PREENCHIDA ####################
        self.getDtEntrada = QtWidgets.QLineEdit(self.groupBox_2)
        self.getDtEntrada.setGeometry(QtCore.QRect(80, 60, 113, 20))
        self.getDtEntrada.setObjectName("Data de entrada")
        self.getDtEntrada.setText(dt_gen())
        self.getHrEntrada = QtWidgets.QLineEdit(self.groupBox_2)
        self.getHrEntrada.setGeometry(QtCore.QRect(80, 80, 113, 20))
        self.getHrEntrada.setObjectName("Hora de Entrada")
        self.getHrEntrada.setText(hm_gen())  ######### JÁ VEM COM A HORA DE ENTRADA PREENCHIDA ####################
        #self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        #self.pushButton.setGeometry(QtCore.QRect(20, 140, 156, 23))
        #self.pushButton.setObjectName("pushBotton")
        #self.pushButton.clicked.connect(self.okAndClose)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.groupBox_2)
        self.buttonBox.setGeometry(QtCore.QRect(20, 150, 156, 23))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox_2")
        self.buttonBox.accepted.connect(self.okAndClose)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Registro de Saída"))
        #self.buttonBox.setText(_translate("Form", "Cadastrar"))
        self.groupBox_2.setTitle(_translate("Form", "Entrada"))
        self.Placa.setText(_translate("Form", "Placa"))
        self.Box.setText(_translate("Form", "Nº do Box"))
        self.DtEntrada.setText(_translate("Form", "D. Entrada"))
        self.HrEntrada.setText(_translate("Form", "H. Entrada"))

    def okAndClose(self):
        self.inserirDados()
        Form.close()

    # FUNÇÃO PARA INSERIR DADOS NO BANCO
    def inserirDados(self):
        # Nesta função criei um banco interno a este arquivo,
        # ou seja, o banco esta rodando tudo dentro desta função
        db = sqlite3.connect('bancoEstacionamento.db')
        itensDicio = self.getinfo()
        print(itensDicio)
        db.cursor()
        db.execute("""INSERT INTO placas (
                          placa,
                          d_entrada,
                          h_entrada,
                          box_util
                      )
                      VALUES (?,?,?,?)
                      """,
                   (itensDicio['placa'], itensDicio['d_entrada'], itensDicio['h_entrada'], itensDicio['box']))
        db.commit()
        db.close()


    # Busca os dados criados para entrada do automovel
    def getinfo(self):
        self.itensDicio = {"placa": self.getPlaca.text(), "box": self.getBox.text(), "d_entrada" : self.getDtEntrada.text(), "h_entrada" : self.getHrEntrada.text()}
        return self.itensDicio


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Entrada()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
"""from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from GUI.entradaui import Ui_Entrada


Aplicacao = QApplication([])
mainWindow = QMainWindow()


mainWindow.setWindowTitle('PRIMEIRA TELA')
mainWindow.setGeometry(20, 50, 800, 600)

botao01 = QPushButton(mainWindow)
botao01.setText('ABRE NOVA JANELA')
botao01.setGeometry(300, 200, 150, 100)

newWindow = Ui_Entrada()
newWindow.rodaSis()


from geraPlaca import placa_gen, box_gen, hm_gen, dt_gen
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Entrada(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(224, 199)
        self.itensDicio = None
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
        self.buttonBox = QtWidgets.QDialogButtonBox(self.groupBox_2)
        self.buttonBox.setGeometry(QtCore.QRect(20, 140, 156, 23))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.accepted.connect(self.getinfo)
        self.buttonBox.accepted.connect(exit)
        self.buttonBox.rejected.connect(exit)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def getinfo(self):
        self.itensDicio = {"placa": self.getPlaca.text(), "box": self.getBox.text(), "d_entrada" : self.getDtEntrada.text(), "h_entrada" : self.getHrEntrada.text()}

        #### Conectar e gravar no banco ####

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Registro de Saída"))
        self.groupBox_2.setTitle(_translate("Form", "Entrada"))
        self.Placa.setText(_translate("Form", "Placa"))
        self.Box.setText(_translate("Form", "Nº do Box"))
        self.DtEntrada.setText(_translate("Form", "D. Entrada"))
        self.HrEntrada.setText(_translate("Form", "H. Entrada"))

    def rodaSis(self):
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        ui = Ui_Entrada()
        ui.setupUi(Form)
        Form.show()
        sys.exit(app.exec_())

newWindow = Ui_Entrada()

def abre():
    newWindow.rodaSis()

botao01.clicked.connect(abre)


mainWindow.show()
Aplicacao.exec_()"""

import sqlite3


class Banco:
    def __init__(self):
        self.conexao = sqlite3.connect('Banco.db')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()

        c.execute("""create table if not exists usuarios(
                    idusuario integer primary key autoincrement,
                    nome text,
                    telefone text,
                    email text,
                    usuario text,
                    senha text)""")

        c.execute("""create table if not exists cidade(
                     idcidade integer primary key  autoincrement,
                     nome text)""")

        self.conexao.commit()
        c.close()

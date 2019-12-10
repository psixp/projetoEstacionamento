#from banco import Banco
from geraPlaca import placa_gen, box_gen, hm_gen
from PyQt5 import QtCore, QtGui, QtWidgets
from GUI.driveboxui import Ui_MainWindow
from GUI.entradaui import Ui_Entrada
from GUI.saidaui import Ui_Saida


def mainWindow():
    if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())


def teste():
    if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        ui = Ui_Entrada()
        ui.setupUi(Form)
        Form.show()
        sys.exit(app.exec_())
#mainWindow()
teste()
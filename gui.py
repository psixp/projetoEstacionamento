from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QDialog
import sys
class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('DriveBox.ui', self)
        self.show()

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
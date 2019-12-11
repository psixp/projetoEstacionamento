from GUI import entradaui
from geraPlaca import placa_gen, box_gen, hm_gen, dt_gen
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from GUI.entradaui import Ui_Entrada
from GUI.saidaui import Ui_Saida
from banco import Database


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, Form, Form2Saida):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(358, 399)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
########################################################################################################################
      # INICIO DO MAIN WINDOW / PAGINA INICIAL DO PROJETO #
########################################################################################################################
        self.boxusos = Database("bancoEstacionamento.db").getBoxsUso()
        self.percent = self.getpercent(len(self.boxusos))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(5, 5, 211, 351))
        self.groupBox.setObjectName("groupBox")
        self.label_1 = QtWidgets.QLabel(self.groupBox)
        self.label_1.setGeometry(QtCore.QRect(10, 20, 41, 21))
        self.label_1.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.progressBar = QtWidgets.QProgressBar(self.groupBox)
        self.progressBar.setGeometry(QtCore.QRect(10, 320, 191, 23))
        self.progressBar.setProperty("value", self.getpercent(len(self.boxusos)))
        self.progressBar.setObjectName("progressBar")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 41, 21))
        self.label_2.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 41, 21))
        self.label_3.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 110, 41, 21))
        self.label_4.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 140, 41, 21))
        self.label_5.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 170, 41, 21))
        self.label_6.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(10, 200, 41, 21))
        self.label_7.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(10, 230, 41, 21))
        self.label_8.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(10, 260, 41, 21))
        self.label_9.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(10, 290, 41, 21))
        self.label_10.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(60, 20, 41, 21))
        self.label_11.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(60, 50, 41, 21))
        self.label_12.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(60, 80, 41, 21))
        self.label_13.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setGeometry(QtCore.QRect(60, 110, 41, 21))
        self.label_14.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        self.label_15.setGeometry(QtCore.QRect(60, 140, 41, 21))
        self.label_15.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.groupBox)
        self.label_16.setGeometry(QtCore.QRect(60, 170, 41, 21))
        self.label_16.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.groupBox)
        self.label_17.setGeometry(QtCore.QRect(60, 200, 41, 21))
        self.label_17.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.groupBox)
        self.label_18.setGeometry(QtCore.QRect(60, 230, 41, 21))
        self.label_18.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.groupBox)
        self.label_19.setGeometry(QtCore.QRect(60, 260, 41, 21))
        self.label_19.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.groupBox)
        self.label_20.setGeometry(QtCore.QRect(60, 290, 41, 21))
        self.label_20.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"font: 12pt \"MS Shell Dlg 2\";\n")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.groupBox)
        self.label_21.setGeometry(QtCore.QRect(110, 20, 41, 21))
        self.label_21.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.groupBox)
        self.label_22.setGeometry(QtCore.QRect(110, 50, 41, 21))
        self.label_22.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.groupBox)
        self.label_23.setGeometry(QtCore.QRect(110, 80, 41, 21))
        self.label_23.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.groupBox)
        self.label_24.setGeometry(QtCore.QRect(110, 110, 41, 21))
        self.label_24.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.groupBox)
        self.label_25.setGeometry(QtCore.QRect(110, 140, 41, 21))
        self.label_25.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.groupBox)
        self.label_26.setGeometry(QtCore.QRect(110, 170, 41, 21))
        self.label_26.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.groupBox)
        self.label_27.setGeometry(QtCore.QRect(110, 200, 41, 21))
        self.label_27.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.groupBox)
        self.label_28.setGeometry(QtCore.QRect(110, 230, 41, 21))
        self.label_28.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.groupBox)
        self.label_29.setGeometry(QtCore.QRect(110, 260, 41, 21))
        self.label_29.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.groupBox)
        self.label_30.setGeometry(QtCore.QRect(110, 290, 41, 21))
        self.label_30.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.groupBox)
        self.label_31.setGeometry(QtCore.QRect(160, 20, 41, 21))
        self.label_31.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.groupBox)
        self.label_32.setGeometry(QtCore.QRect(160, 50, 41, 21))
        self.label_32.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_32.setAlignment(QtCore.Qt.AlignCenter)
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.groupBox)
        self.label_33.setGeometry(QtCore.QRect(160, 80, 41, 21))
        self.label_33.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_33.setAlignment(QtCore.Qt.AlignCenter)
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.groupBox)
        self.label_34.setGeometry(QtCore.QRect(160, 110, 41, 21))
        self.label_34.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_34.setAlignment(QtCore.Qt.AlignCenter)
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self.groupBox)
        self.label_35.setGeometry(QtCore.QRect(160, 140, 41, 21))
        self.label_35.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_35.setAlignment(QtCore.Qt.AlignCenter)
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.groupBox)
        self.label_36.setGeometry(QtCore.QRect(160, 170, 41, 21))
        self.label_36.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_36.setAlignment(QtCore.Qt.AlignCenter)
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.groupBox)
        self.label_37.setGeometry(QtCore.QRect(160, 200, 41, 21))
        self.label_37.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.groupBox)
        self.label_38.setGeometry(QtCore.QRect(160, 230, 41, 21))
        self.label_38.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_38.setAlignment(QtCore.Qt.AlignCenter)
        self.label_38.setObjectName("label_38")
        self.label_39 = QtWidgets.QLabel(self.groupBox)
        self.label_39.setGeometry(QtCore.QRect(160, 260, 41, 21))
        self.label_39.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_39.setAlignment(QtCore.Qt.AlignCenter)
        self.label_39.setObjectName("label_39")
        self.label_40 = QtWidgets.QLabel(self.groupBox)
        self.label_40.setGeometry(QtCore.QRect(160, 290, 41, 21))
        self.label_40.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_40.setAlignment(QtCore.Qt.AlignCenter)
        self.label_40.setObjectName("label_40")
        self.labels = {
            "1": self.label_1, "2": self.label_2, "3": self.label_3, "4": self.label_4, "5": self.label_5,
            "6": self.label_6, "7": self.label_7, "8": self.label_8, "9": self.label_9, "10": self.label_10,
            "11": self.label_11, "12": self.label_12, "13": self.label_13, "14": self.label_14, "15": self.label_15,
            "16": self.label_16, "17": self.label_17, "18": self.label_18, "19": self.label_19, "20": self.label_20,
            "21": self.label_21, "22": self.label_22, "23": self.label_23, "24": self.label_24, "25": self.label_25,
            "26": self.label_6, "27": self.label_7, "28": self.label_8, "29": self.label_9, "30": self.label_30,
            "31": self.label_31, "32": self.label_32, "33": self.label_33, "34": self.label_34, "35": self.label_35,
            "36": self.label_36, "37": self.label_37, "38": self.label_38, "39": self.label_39, "40": self.label_40
        } # TEM UM DICIONARIO COM AS LABELS DE TODOS OS BOX SEGUIDO POR {"Nº-BOX" : SELF.LABEL}
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(220, 5, 131, 181))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 111, 151))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.PBentrada = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.PBentrada.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.PBentrada.setObjectName("PBentrada")
        self.verticalLayout.addWidget(self.PBentrada)
        self.PBsaida = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.PBsaida.setObjectName("PBsaida")
        self.verticalLayout.addWidget(self.PBsaida)
        self.PBconspl = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.PBconspl.setObjectName("PBconspl")
        self.verticalLayout.addWidget(self.PBconspl)
        self.PBconsbx = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.PBconsbx.setObjectName("PBconsbx")
        self.verticalLayout.addWidget(self.PBconsbx)
        self.updatenum = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.updatenum.setObjectName("updatenum")
        self.verticalLayout.addWidget(self.updatenum)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 358, 18))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuOp_es = QtWidgets.QMenu(self.menubar)
        self.menuOp_es.setObjectName("menuOp_es")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionCadastrar_Entrada = QtWidgets.QAction(MainWindow)
        self.actionCadastrar_Entrada.setObjectName("actionCadastrar_Entrada")
        self.actionCadastrar_Sa_da = QtWidgets.QAction(MainWindow)
        self.actionCadastrar_Sa_da.setObjectName("actionCadastrar_Sa_da")
        self.actionFechar_Programa = QtWidgets.QAction(MainWindow)
        self.actionFechar_Programa.setObjectName("actionFechar_Programa")
        self.actionConsultar_Placa = QtWidgets.QAction(MainWindow)
        self.actionConsultar_Placa.setObjectName("actionConsultar_Placa")
        self.actionConsultar_box = QtWidgets.QAction(MainWindow)
        self.actionConsultar_box.setObjectName("actionConsultar_box")
        self.menuMenu.addAction(self.actionCadastrar_Entrada)
        self.menuMenu.addAction(self.actionCadastrar_Sa_da)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionConsultar_Placa)
        self.menuMenu.addAction(self.actionConsultar_box)
        self.menuOp_es.addAction(self.actionFechar_Programa)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuOp_es.menuAction())
        self.PBentrada.clicked.connect(self.initEntradaUi)
        self.PBsaida.clicked.connect(self.initSaidaUi)
        #self.PBconspl.clicked.connect(self.SetColorRedBox())
        #self.PBconsbx.clicked.connect(self.testando)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
########################################################################################################################
# INICIO DO WIDGET DE ENTRADA #
########################################################################################################################
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
        self.getBox = QtWidgets.QLineEdit(self.groupBox_2)
        self.getBox.setGeometry(QtCore.QRect(80, 40, 113, 20))
        self.getBox.setObjectName("BOX")
        self.getDtEntrada = QtWidgets.QLineEdit(self.groupBox_2)
        self.getDtEntrada.setGeometry(QtCore.QRect(80, 60, 113, 20))
        self.getDtEntrada.setObjectName("Data de entrada")
        self.getHrEntrada = QtWidgets.QLineEdit(self.groupBox_2)
        self.getHrEntrada.setGeometry(QtCore.QRect(80, 80, 113, 20))
        self.getHrEntrada.setObjectName("Hora de Entrada")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(20, 140, 156, 23))
        self.pushButton.setObjectName("pushBotton")
        self.pushButton.clicked.connect(self.okAndClose)
        self.boxteste = ""
        self.SetColorUtilBox()

        self.retranslateUi2(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
########################################################################################################################
# INICIO DO WIDGET DE SAIDA #
########################################################################################################################
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
        #self.saidaplaca.setText("QNI9812")
        self.boxsaida = QtWidgets.QLineEdit(self.groupBox_3)
        self.boxsaida.setGeometry(QtCore.QRect(80, 40, 113, 20))
        self.boxsaida.setObjectName("boxsaida")
        #self.boxsaida.setText("importar box do banco")
        self.dtEntrSaida = QtWidgets.QLineEdit(self.groupBox_3)
        self.dtEntrSaida.setGeometry(QtCore.QRect(80, 60, 113, 20))
        self.dtEntrSaida.setObjectName("dtEntrSaida")
        #self.dtEntrSaida.setText("importar box do banco")
        self.hSaidaSai = QtWidgets.QLineEdit(self.groupBox_3)
        self.hSaidaSai.setGeometry(QtCore.QRect(80, 80, 113, 20))
        self.hSaidaSai.setObjectName("hSaidaSai")
        #self.hSaidaSai.setText("importar box do banco")
        self.dtSaidaSai = QtWidgets.QLineEdit(self.groupBox_3)
        self.dtSaidaSai.setGeometry(QtCore.QRect(80, 100, 113, 20))
        self.dtSaidaSai.setObjectName("dtSaidaSai")
        #self.dtSaidaSai.setText("importar box do banco")
        self.hEntrSaida = QtWidgets.QLineEdit(self.groupBox_3)
        self.hEntrSaida.setGeometry(QtCore.QRect(80, 120, 113, 20))
        self.hEntrSaida.setObjectName("hEntrSaida")
        #self.hEntrSaida.setText("importar box do banco")
        #self.buttonBox_2 = QtWidgets.QDialogButtonBox(self.groupBox_3)
        #self.buttonBox_2.setGeometry(QtCore.QRect(20, 150, 156, 23))
        #self.buttonBox_2.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        #self.buttonBox_2.setObjectName("buttonBox_2")
        self.buscarPlaca = QtWidgets.QPushButton(Form2Saida)
        self.buscarPlaca.setGeometry(QtCore.QRect(40, 160, 60, 23))
        self.buscarPlaca.setObjectName("buscarPlaca")
        self.buscarPlaca.clicked.connect(self.buscarsaidaplacabox)
        self.gravaSaida = QtWidgets.QPushButton(Form2Saida)
        self.gravaSaida.setGeometry(QtCore.QRect(120, 160, 60, 23))
        self.gravaSaida.setObjectName("gravaSaida")
        self.gravaSaida.clicked.connect(self.updatesaida)


        self.retranslateUi3(Form2Saida)
        QtCore.QMetaObject.connectSlotsByName(Form2Saida)

    # NOMES DE LINHAS E BOTOES PAGINA PRINCIPAL
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DriveBox"))
        self.groupBox.setTitle(_translate("MainWindow", "Relação de Box"))
        self.label_1.setText(_translate("MainWindow", "01"))
        self.label_2.setText(_translate("MainWindow", "02"))
        self.label_3.setText(_translate("MainWindow", "03"))
        self.label_4.setText(_translate("MainWindow", "04"))
        self.label_5.setText(_translate("MainWindow", "05"))
        self.label_6.setText(_translate("MainWindow", "06"))
        self.label_7.setText(_translate("MainWindow", "07"))
        self.label_8.setText(_translate("MainWindow", "08"))
        self.label_9.setText(_translate("MainWindow", "09"))
        self.label_10.setText(_translate("MainWindow", "10"))
        self.label_11.setText(_translate("MainWindow", "11"))
        self.label_12.setText(_translate("MainWindow", "12"))
        self.label_13.setText(_translate("MainWindow", "13"))
        self.label_14.setText(_translate("MainWindow", "14"))
        self.label_15.setText(_translate("MainWindow", "15"))
        self.label_16.setText(_translate("MainWindow", "16"))
        self.label_17.setText(_translate("MainWindow", "17"))
        self.label_18.setText(_translate("MainWindow", "18"))
        self.label_19.setText(_translate("MainWindow", "19"))
        self.label_20.setText(_translate("MainWindow", "20"))
        self.label_21.setText(_translate("MainWindow", "21"))
        self.label_22.setText(_translate("MainWindow", "22"))
        self.label_23.setText(_translate("MainWindow", "23"))
        self.label_24.setText(_translate("MainWindow", "24"))
        self.label_25.setText(_translate("MainWindow", "25"))
        self.label_26.setText(_translate("MainWindow", "26"))
        self.label_27.setText(_translate("MainWindow", "27"))
        self.label_28.setText(_translate("MainWindow", "28"))
        self.label_29.setText(_translate("MainWindow", "29"))
        self.label_30.setText(_translate("MainWindow", "30"))
        self.label_31.setText(_translate("MainWindow", "31"))
        self.label_32.setText(_translate("MainWindow", "32"))
        self.label_33.setText(_translate("MainWindow", "33"))
        self.label_34.setText(_translate("MainWindow", "34"))
        self.label_35.setText(_translate("MainWindow", "35"))
        self.label_36.setText(_translate("MainWindow", "36"))
        self.label_37.setText(_translate("MainWindow", "37"))
        self.label_38.setText(_translate("MainWindow", "38"))
        self.label_39.setText(_translate("MainWindow", "39"))
        self.label_40.setText(_translate("MainWindow", "40"))
        self.groupBox_2.setTitle(_translate("MainWindow", "GroupBox"))
        self.PBentrada.setText(_translate("MainWindow", "Registrar Entrada"))
        self.PBsaida.setText(_translate("MainWindow", "Registrar Saída"))
        self.PBconspl.setText(_translate("MainWindow", "Consultar Placa"))
        self.PBconsbx.setText(_translate("MainWindow", "Consultar Box"))
        self.updatenum.setText(_translate("MainWindow", "Atualizar Dados"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.menuOp_es.setTitle(_translate("MainWindow", "Opções"))
        self.actionCadastrar_Entrada.setText(_translate("MainWindow", "Cadastrar Entrada"))
        self.actionCadastrar_Sa_da.setText(_translate("MainWindow", "Cadastrar Saída"))
        self.actionFechar_Programa.setText(_translate("MainWindow", "Fechar Programa"))
        self.actionConsultar_Placa.setText(_translate("MainWindow", "Consultar Placa"))
        self.actionConsultar_box.setText(_translate("MainWindow", "Consultar box"))
    # NOMES DE LINHAS E BOTOES ENTRADA
    def retranslateUi2(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Registro de Saída"))
        self.pushButton.setText(_translate("Form", "Cadastrar"))
        self.groupBox_2.setTitle(_translate("Form", "Entrada"))
        self.Placa.setText(_translate("Form", "Placa"))
        self.Box.setText(_translate("Form", "Nº do Box"))
        self.DtEntrada.setText(_translate("Form", "D. Entrada"))
        self.HrEntrada.setText(_translate("Form", "H. Entrada"))
    # NOMES DE LINHAS E BOTOES SAIDA
    def retranslateUi3(self, Form2Saida):
        _translate = QtCore.QCoreApplication.translate
        Form2Saida.setWindowTitle(_translate("Form", "Registro de Entrada"))
        self.groupBox_3.setTitle(_translate("Form", "Saída"))
        self.placa.setText(_translate("Form", "Placa"))
        self.box.setText(_translate("Form", "Nº do Box"))
        self.hrSaida.setText(_translate("Form", "H. Saída"))
        self.dtEntrada.setText(_translate("Form", "D. Entrada"))
        self.dtSaida.setText(_translate("Form", "D. Saída"))
        self.hrEntrada.setText(_translate("Form", "H. Entrada"))
        self.buscarPlaca.setText(_translate("Form", "Buscar"))
        self.gravaSaida.setText(_translate("Form", "Saida"))

    def getpercent(self, ttl):
        percent = ttl / 40 * 100
        #print(len(self.boxusos))
        return percent

    # DEFINE A COR DA CAIXA DE NUMERO DO BOX
    def SetColorRedBox(self, boxgerado): # UTILIZADA NO BOTAO CADASTRAR ENTRADA
        #box = boxgerado # alterar depois para retorno do entradaui.pycom Nº do BOX
        self.labels[boxgerado].setStyleSheet("background-color: rgb(170, 0, 0); font: 75 12pt \"MS Shell Dlg 2\";")

    # DEFINE A COR DA CAIXA DE NUMERO DO BOX
    def SetColorGreenBox(self, boxgerado): # UTILIZADA NO BOTAO CADASTRAR SAIDA
        # box = box_gen() # alterar depois para consulta banco
        self.labels[boxgerado].setStyleSheet("background-color: rgb(0, 170, 0); font: 75 12pt \"MS Shell Dlg 2\";")

    # PINTAR BOX EM UTILIZAÇÃO NA INICIALIZAÇÃO
    def SetColorUtilBox(self):
        ttl = len(self.boxusos)
        self.percent = self.getpercent(ttl)
        for x in range(ttl):
            self.SetColorRedBox(str(self.boxusos[x]))

    # INICIALIZA AQ CLASSE ENTRADA PARA CADASTRAR A ENTRADA
    # ERA PRA CARREGAR A CLASSE COMO ESTA NO UI_ENTRADA...
    # MAS NAO ESTA EFETUANDO AS MESMAS FUNCIONALIDADES QUE EXECUTAR NO PROPRIO ARQUIVO.
    def initEntradaUi(self):
        Form.showNormal()
        self.getPlaca.setText(placa_gen())   ######### JÁ VEM COM A PLACA PREENCHIDA ####################
        self.getBox.setText(box_gen())       ######### JÁ VEM COM A BOX PREENCHIDA ####################
        self.getDtEntrada.setText(dt_gen())  ######### JÁ VEM COM A DATA DE ENTRADA PREENCHIDA ####################
        self.getHrEntrada.setText(hm_gen())  ######### JÁ VEM COM A HORA DE ENTRADA PREENCHIDA ####################

    # INICIALIZA AQ CLASSE ENTRADA PARA CADASTRAR A SAIDA DOS AUTOMOVEIS
    def initSaidaUi(self):
        Form2Saida.showNormal()
        self.getPlaca.setText(placa_gen())  ######### JÁ VEM COM A PLACA PREENCHIDA ####################
        self.getBox.setText(box_gen())  ######### JÁ VEM COM A BOX PREENCHIDA ####################
        self.getDtEntrada.setText(dt_gen())  ######### JÁ VEM COM A DATA DE ENTRADA PREENCHIDA ####################
        self.getHrEntrada.setText(hm_gen())  ######### JÁ VEM COM A HORA DE ENTRADA PREENCHIDA ####################

###################################################################################################
###################################################################################################
## FUNÇÕES DE ENTRADA
###################################################################################################
    # Confirma os Dados e fecha janela
    def okAndClose(self):
        itensDicio = self.getinfo()
        self.inserirDados(itensDicio)
        self.SetColorRedBox(itensDicio["box"])
        Form.close()

    # FUNÇÃO PARA INSERIR DADOS NO BANCO
    def inserirDados(self, itensDicio):
        insert = Database("bancoEstacionamento.db")
        insert.insertDadosDiaria(itensDicio)

    # Busca os dados criados para entrada do automovel
    def getinfo(self):
        self.itensDicio = {"placa": self.getPlaca.text(), "box": self.getBox.text(), "d_entrada" : self.getDtEntrada.text(), "h_entrada" : self.getHrEntrada.text()}
        return self.itensDicio

    #def testando(self):
    #    self.SetColorUtilBox()
###################################################################################################
###################################################################################################
## FUNÇÕES DE SAIDA
###################################################################################################
    def buscarsaidaplacabox(self):
        itembusca = {"placa": str(self.saidaplaca.text())}
        #itembusca = {"placa": "QNI9812"}
        db = Database("bancoEstacionamento.db")
        db.getDadosRow(itembusca["placa"])
        self.boxsaida.setText(str(db.setBoxDB))
        self.dtEntrSaida.setText(db.setDEntradaDB)
        self.hEntrSaida.setText(db.setHEntradaDB)
        self.hSaidaSai.setText(hm_gen())
        self.dtSaidaSai.setText(dt_gen())


    def updatesaida(self):
        db = Database("bancoEstacionamento.db")
        #print([self.dtSaidaSai.text(), self.hSaidaSai.text(), self.saidaplaca.text()])
        #db.updateDadosSaida((self.dtSaidaSai.text(), self.hSaidaSai.text(), self.saidaplaca.text()))
        self.updateSaidaInsertLogg()

    def updateSaidaInsertLogg(self):
        db = Database("bancoEstacionamento.db")
        itensDicio = {"placa": self.saidaplaca.text(), "d_entrada": self.dtEntrSaida.text(), "h_entrada": self.hEntrSaida.text(), "d_saida": self.dtSaidaSai.text(), "h_saida": self.hSaidaSai.text(), "v_pago": "10", "box": self.getBox.text(),}
        db.insertDadosLogg(itensDicio)
        db.deletarDados(itensDicio)
        Form2Saida.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow() # CARREGA O GUI EM UMA VARIAVEL
    Form = QtWidgets.QWidget() # CARREGA O GUI DE ENTRADA
    Form2Saida = QtWidgets.QWidget() # CARREGA O GUI DE SAIDA
    saidainit = QtWidgets.QWidget() # CARREGA O GUI EM UMA VARIAVEL
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, Form, Form2Saida)
    #MainWindow.showNormal()
    #Form.showNormal()
    Form2Saida.showNormal()
    #ui.buscarsaidaplacabox()
    sys.exit(app.exec_())
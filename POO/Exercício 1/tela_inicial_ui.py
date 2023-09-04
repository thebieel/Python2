# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_inicial.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################


import sys
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QWidget,QDialog,QVBoxLayout)


from funcoes import depositar

class Ui_telainicial(object):
    def setupUi(self,telainicial):
        if not telainicial.objectName():
            telainicial.setObjectName(u"telainicial")
        telainicial.resize(565, 454)
        telainicial.setMinimumSize(QSize(565, 454))
        telainicial.setMaximumSize(QSize(565, 454))
        self.centralwidget = QWidget(telainicial)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(375, 429))
        self.centralwidget.setMaximumSize(QSize(375, 429))
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(9, 9, 565, 454))
        self.frame.setMinimumSize(QSize(565, 454))
        self.frame.setMaximumSize(QSize(565, 454))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.lbl_nc = QLabel(self.frame)
        self.lbl_nc.setObjectName(u"lbl_nc")
        self.lbl_nc.setGeometry(QRect(20, 70, 86, 20))
        self.lbl_nc.setMinimumSize(QSize(150, 20))
        self.lbl_nc.setMaximumSize(QSize(100, 20))
        font = QFont()
        font.setFamilies([u"MS Shell Dlg 2"])
        self.lbl_nc.setFont(font)
        self.lbl_nc.setTextFormat(Qt.AutoText)
        self.input_nc = QLineEdit(self.frame)
        self.input_nc.setObjectName(u"input_nc")
        self.input_nc.setGeometry(QRect(10, 98, 133, 20))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_nc.sizePolicy().hasHeightForWidth())
        self.input_nc.setSizePolicy(sizePolicy)
        self.input_nc.setMinimumSize(QSize(70, 20))
        self.input_nc.setMaximumSize(QSize(150, 20))
        self.btn_dep = QPushButton(self.frame)
        self.btn_dep.setObjectName(u"btn_dep")
        self.btn_dep.setGeometry(QRect(10, 310, 100, 20))
        self.btn_dep.setMinimumSize(QSize(70, 20))
        self.btn_dep.setMaximumSize(QSize(100, 20))
        self.btn_saq = QPushButton(self.frame)
        self.btn_saq.setObjectName(u"btn_saq")
        self.btn_saq.setGeometry(QRect(10, 350, 100, 20))
        self.btn_saq.setMinimumSize(QSize(70, 20))
        self.btn_saq.setMaximumSize(QSize(100, 20))
        self.input_nt = QLineEdit(self.frame)
        self.input_nt.setObjectName(u"input_nt")
        self.input_nt.setGeometry(QRect(10, 174, 133, 20))
        self.input_nt.setMinimumSize(QSize(70, 20))
        self.input_nt.setMaximumSize(QSize(150, 20))
        self.input_dpi = QLineEdit(self.frame)
        self.input_dpi.setObjectName(u"input_dpi")
        self.input_dpi.setGeometry(QRect(10, 250, 133, 20))
        self.input_dpi.setMinimumSize(QSize(70, 20))
        self.input_dpi.setMaximumSize(QSize(150, 20))
        self.lbl_nt = QLabel(self.frame)
        self.lbl_nt.setObjectName(u"lbl_nt")
        self.lbl_nt.setGeometry(QRect(20, 140, 77, 20))
        self.lbl_nt.setMinimumSize(QSize(150, 20))
        self.lbl_nt.setMaximumSize(QSize(100, 20))
        self.lbl_dpi = QLabel(self.frame)
        self.lbl_dpi.setObjectName(u"lbl_dpi")
        self.lbl_dpi.setGeometry(QRect(20, 210, 74, 20))
        self.lbl_dpi.setMinimumSize(QSize(150, 20))
        self.lbl_dpi.setMaximumSize(QSize(100, 20))
        self.lbl_sal = QLabel(self.frame)
        self.lbl_sal.setGeometry(QRect(30, 20, 82, 20))
        self.lbl_sal.setMinimumSize(QSize(150, 20))
        self.lbl_sal.setMaximumSize(QSize(100, 20))
        self.label_saldo = self.lbl_sal
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setBold(True)
        font1.setItalic(True)
        self.lbl_opc = QLabel(self.frame)
        self.lbl_opc.setObjectName(u"lbl_opc")
        self.lbl_opc.setEnabled(True)
        self.lbl_opc.setGeometry(QRect(20, 230, 56, 16))
        self.lbl_opc.setMinimumSize(QSize(100, 7))
        self.lbl_opc.setMaximumSize(QSize(100, 20))
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 330, 47, 13))
        telainicial.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(telainicial)
        self.statusBar.setObjectName(u"statusBar")
        telainicial.setStatusBar(self.statusBar)

        self.retranslateUi(telainicial)

        QMetaObject.connectSlotsByName(telainicial)

    def retranslateUi(self, telainicial):
        telainicial.setWindowTitle(QCoreApplication.translate("telainicial", u"MainWindow", None))
        self.lbl_nc.setText(QCoreApplication.translate("telainicial", u"N\u00famero da conta:", None))
        self.btn_dep.setText(QCoreApplication.translate("telainicial", u"Dep\u00f3sito", None))
        self.btn_saq.setText(QCoreApplication.translate("telainicial", u"Saque", None))
        self.lbl_nt.setText(QCoreApplication.translate("telainicial", u"Nome do titular:", None))
        self.lbl_dpi.setText(QCoreApplication.translate("telainicial", u"Dep\u00f3sito inicial:", None))
        self.lbl_opc.setText(QCoreApplication.translate("telainicial", u"   (opcional)", None))
        self.lbl_sal.setText(QCoreApplication.translate(f"telainicial", u"Saldo atual: R$ 0.00", None))
        
        
        
        
class tela_deposito(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
        
    def initUI(self,):
        self.setWindowTitle('Página de Depósito')
        self.setGeometry(100, 100, 400, 200)

        self.label_saldo = QLabel('Saldo atual: R$ 0.00', self)
        self.label_saldo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label_quantia = QLabel('Quantia a depositar:', self)
        self.input_quantia = QLineEdit(self)
        self.input_quantia.setPlaceholderText('Digite o valor do depósito:')

        self.btn_depositar = QPushButton('Depositar', self)
        self.btn_depositar.clicked.connect(depositar)

        layout = QVBoxLayout()
        layout.addWidget(self.label_saldo)
        layout.addWidget(self.label_quantia)
        layout.addWidget(self.input_quantia)
        layout.addWidget(self.btn_depositar)
        self.setLayout(layout)

        self.saldo = 0.00
        
class TelaInicial(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.ui = (Ui_telainicial)
        self.ui.setupUi(self)
        
        self.saldo_atual = 0.00
        
        self.ui.btn_dep.clicked.connect(self.depositar)
        
        self.atualizar_saldo()

    def realizar_deposito(self):
        try:
            valor_deposito = float(self.ui.input_dpi.text())
            if valor_deposito > 0:
                self.saldo_atual = depositar(self.saldo_atual, valor_deposito)  # Chama a função depositar com os parâmetros corretos
                self.atualizar_saldo()
            else:
                self.ui.label.setText("Digite um valor válido.")
        except ValueError:
            self.ui.label.setText("Digite um valor numérico válido.")

    def atualizar_saldo(self):
        self.ui.label.setText(f"Saldo atual: R$ {self.saldo_atual:.2f}")
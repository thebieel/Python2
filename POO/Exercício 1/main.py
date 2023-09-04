from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QWidget
from tela_inicial_ui import Ui_telainicial
from tela_inicial_ui import tela_deposito
import sys

class MainWindow(QMainWindow, Ui_telainicial):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Spoinner Bank')
        self.btn_dep.clicked.connect(self.mostrar_tela_deposito)  

    def mostrar_tela_deposito(self):
        self.tela_dep = tela_deposito()
        self.tela_dep.show()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
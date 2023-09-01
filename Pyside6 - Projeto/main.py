from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon 
from projeto import Ui_MainWindow
import shutil
import sys
import os


class MainWindow(QMainWindow, Ui_MainWindow) :
    def init (self):
        super(). init ()
        self.setupUi(self)
        self.setWindowTitle("Organizador de Arquivo")
        appIcon = QIcon("folder.png")
        self.setWindowIcon(appIcon)
        self.btn_01.clicked.connect(self.open_path)
        self.btn_02.clicked.connect(self.open_path)
        
    def open_path(self):
        self.path = QFileDialog.getExistingDirectory(self, str('pasta com arquivos'), '/home', QFileDialog.ShowDirsOnly | 
        QFileDialog.DontResolveSymlinks)
        self.txt_path.setText(self.path)
        self.path = str(self.path)
        
        
        
app = QApplication(sys.argv)
janela = MainWindow()
janela.show()
app.exec()
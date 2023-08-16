from logintela import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QFrame, QLabel, QLineEdit,QMainWindow, QSizePolicy, QVBoxLayout, QWidget
import sys


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Tela Login")
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(w)
    w.show()
    app.exec()
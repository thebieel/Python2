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
from tela_inicial_ui import Ui_telainicial
from funcoes import depositar

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
        
        # Inicializa o saldo atual como 0.00
        self.saldo_atual = 0.00
        self.ui.btn_dep.clicked.connect(self.realizar_deposito)
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
            self.ui.label.setText("Digite somente números.")

    def atualizar_saldo(self):
        self.ui.label.setText(f"Saldo atual: R$ {self.saldo_atual:.2f}")


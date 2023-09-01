import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit, QDialog


class ContaBancaria:
    def __init__(self, numero_conta, nome_titular, saldo_inicial =0):
        self.numero_conta = numero_conta
        self.nome_titular = nome_titular
        self.saldo = saldo_inicial
    
    def deposito(self, valor):
        self.saldo += valor
    
    def saque(self, valor):
        if valor + 5 <= self.saldo:
            self.saldo -= valor + 5
            return True
        else:
            return False

class BancoApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Spoinner Bank")

        self.layout = QVBoxLayout()
        self.central_widget = QWidget
        
        self.label_numero_conta = QLabel("Número da Conta:")
        self.edit_numero_conta = QLineEdit()
        self.layout.addWidget(self.label_numero_conta)
        self.layout.addWidget(self.edit_numero_conta)

        self.label_nome_titular = QLabel("Nome do Titular:")
        self.edit_nome_titular = QLineEdit()
        self.layout.addWidget(self.label_nome_titular)
        self.layout.addWidget(self.edit_nome_titular)

        self.label_saldo = QLabel("Saldo:")
        self.label_saldo_valor = QLabel("0.00")
        self.layout.addWidget(self.label_saldo)
        self.layout.addWidget(self.label_saldo_valor)

        self.deposito_button = QPushButton("Depósito")
        self.saque_button = QPushButton("Saque")
        self.layout.addWidget(self.deposito_button)
        self.layout.addWidget(self.saque_button)
        
        
        self.resultlbl =  QLabel(self)
        self.resultlbl.setGeometry(650,190,170,40)
        
        
        

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

        self.deposito_button.clicked.connect(self.realizar_deposito)
        self.saque_button.clicked.connect(self.realizar_saque)

        self.conta_bancaria = None

    def realizar_deposito(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Página Depósito")
        dialog.setGeometry(200,320,500,400)
        
        dialog_valor_e = QLabel("Digite o valor do depósito",dialog)
        dialog_valor_e.setGeometry(10,10,200,100)
        #valor = float(input("Digite o valor do depósito: "))
        dialog_valor = QLineEdit(dialog)
        dialog_valor.setGeometry(10,70,150,40)
        
        
        if self.conta_bancaria:
            self.conta_bancaria.deposito(dialog.valor)
            self.atualizar_saldo()
            
            
            
        dialog.exec()

    def realizar_saque(self):
        valor = float(input("Digite o valor do saque: "))
        if self.conta_bancaria:
            if self.conta_bancaria.saque(valor):
                print("Saque realizado com sucesso!")
                self.atualizar_saldo()
            else:
                print("Saldo insuficiente para o saque.")

    def atualizar_saldo(self):
        self.label_saldo_valor.setText(f"{self.conta_bancaria.saldo:.2f}")

    def iniciar(self, numero_conta, nome_titular):
        self.conta_bancaria = ContaBancaria(numero_conta, nome_titular)
        self.edit_numero_conta.setText(numero_conta)
        self.edit_nome_titular.setText(nome_titular)
        self.atualizar_saldo()
        
    #def pagina_deposito(self):

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BancoApp()
    window.show()
    sys.exit(app.exec())
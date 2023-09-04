def depositar(saldo_atual, valor_deposito):
    try:
        valor_deposito = float(valor_deposito)
        if valor_deposito > 0:
            saldo_atual += valor_deposito
        return saldo_atual
    except ValueError:
        return saldo_atual




































'''def depositar(self):
        quantia_texto = self.input_quantia.text()
        try:
            quantia = float(quantia_texto)
            if quantia > 0:
                self.saldo += quantia
                self.label_saldo.setText(f'Saldo atual: R$ {self.saldo:.2f}')
            else:
                QMessageBox.warning(self, 'Quantia inválida', 'Digite uma quantia válida maior que zero.')
        except ValueError:
            QMessageBox.warning(self, 'Quantia inválida', 'Digite uma quantia válida.')'''
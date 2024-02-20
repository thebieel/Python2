from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


def fibonacci(n):
    if n < 0:
        return "Por favor, insira um número positivo"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib_sequence = [0, 1]
        for i in range(2, n):
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence[-1]


class FibonacciGameApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=40, spacing=20)

        self.input_label = Label(text="Digite um número para encontrar seu Fibonacci:",
                                 font_size=30,  # Aumento do tamanho da fonte para 30
                                 color=(0, 0, 1, 1))  # Azul
        self.input_text = TextInput(multiline=False,
                                    font_size=30,  # Aumento do tamanho da fonte para 30
                                    size_hint=(1, 0.3))
        self.calculate_button = Button(text="Calcular Fibonacci",
                                       font_size=30,  # Aumento do tamanho da fonte para 30
                                       background_color=(0, 1, 0, 1),  # Verde
                                       size_hint=(1, 0.3))
        self.result_label = Label(text="Resultado aparecerá aqui.",
                                  font_size=30,  # Aumento do tamanho da fonte para 30
                                  color=(1, 0, 0, 1))  # Vermelho

        self.calculate_button.bind(on_press=self.calculate_fibonacci)

        self.layout.add_widget(self.input_label)
        self.layout.add_widget(self.input_text)
        self.layout.add_widget(self.calculate_button)
        self.layout.add_widget(self.result_label)

        return self.layout

    def calculate_fibonacci(self, instance):
        try:
            num = int(self.input_text.text)
            fib_num = fibonacci(num)
            self.result_label.text = f"O Fibonacci de {num} é {fib_num}"
        except ValueError:
            self.result_label.text = "Por favor, insira um número válido."


if __name__ == "__main__":
    FibonacciGameApp().run()

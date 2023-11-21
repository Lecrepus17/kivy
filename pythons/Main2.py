from kivy.uix.screenmanager import Screen

class Main2(Screen):
    def __init__(self, **kwargs):
        super(Main2, self).__init__(**kwargs)

        # Inicialização de variáveis
        self.expression = '0'
        self.display = self.ids['display']

    def update_display(self, value):
        # Atualiza a expressão exibida no widget de display
        if self.expression == '0':
            self.expression = value
        else:
            self.expression += value
        self.display.text = self.expression

    def calculate(self):
        # Tenta calcular a expressão e exibe o resultado ou um erro
        try:
            result = round(eval(self.expression), 3)
            self.display.text = str(result)
            self.expression = str(result)
        except Exception as e:
            self.display.text = 'Error'
            self.expression = '0'

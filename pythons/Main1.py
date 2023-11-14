from kivy.uix.screenmanager import Screen

class Main1(Screen):
    def save(self):
        # Obtém o texto inserido nos widgets com os ids "name" e "text"
        name = str(self.ids["name"].text)
        text = str(self.ids["text"].text)

        # Atualiza os widgets com os ids "name_final" e "text_final" com os valores obtidos
        self.ids["name_final"].text = name
        self.ids["text_final"].text = text

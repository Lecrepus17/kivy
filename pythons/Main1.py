from kivy.uix.screenmanager import Screen
class Main1(Screen):
    def save(self):
        name = str(self.ids["name"].text)
        text = str(self.ids["text"].text)

        self.ids["name_final"].text = name
        self.ids["text_final"].text = text
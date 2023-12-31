from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from pythons.Main1 import Main1
from pythons.List import List
from pythons.custom_transitions import CustomSlideTransition

# Configuração da janela principal
Window.clearcolor = (14 / 255, 61 / 255, 76 / 255, 1)
Window.size = (400, 600)


class MainApp(App):
    def build(self):
        sm = ScreenManager()

        # Adiciona as instâncias das telas ao ScreenManager
        sm.add_widget(Main1(name='main1'))
        sm.add_widget(List(name='list'))

        return sm

    # Função para alternar entre telas
    def switch_screen(self, screen_name, direction):
        sm = self.root  # Obtém a instância do ScreenManager
        sm.transition = CustomSlideTransition(direction)  # Configura a direção da transição
        sm.current = screen_name  # Altera para a tela desejada


# Verifica se o arquivo está sendo executado diretamente
if __name__ == "__main__":
    MainApp().run()

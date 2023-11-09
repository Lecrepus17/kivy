from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from kivy.core.window import Window
from pythons.Main1 import Main1
from pythons.Main2 import Main2
from pythons.custom_transitions import CustomSlideTransition

Window.clearcolor = (14/255, 61/255, 76/255, 1)
Window.size = (400, 600)

class MainApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Main1(name='main1'))
        sm.add_widget(Main2(name='main2'))
        return sm

    def switch_screen(self, screen_name, direction):
        sm = self.root
        sm.transition = CustomSlideTransition(direction)  # Configure a direção da transição
        sm.current = screen_name

if __name__ == "__main__":
    MainApp().run()
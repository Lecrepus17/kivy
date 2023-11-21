from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from Main1 import Main1
from Main2 import Main2

Window.clearcolor = (14/255,61/255,76/255,1)
Window.size = (400,600)

class MainApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Main1(name='main1'))
        sm.add_widget(Main2(name='main2'))
        return sm

if __name__ == "__main__":
    MainApp().run()

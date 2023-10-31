from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
import requests

Window.clearcolor = (14/255,61/255,76/255,1)
Window.size = (400,600)

class Main1(Screen):
    def calc(self):
        pr1 = float(self.ids["pr1"].text)
        ps1 = float(self.ids["ps1"].text)
        pr2 = float(self.ids["pr2"].text)
        ps2 = float(self.ids["ps2"].text)

        self.ids["p1"].text = str(pr1/ps1*1000)
        self.ids["p2"].text = str(pr2/ps2*1000)

        self.ids["dif"].text = str((pr1/ps1)/(pr2/ps2)*100) + ' %'

class Main2(Screen):
    def on_enter(self):
        # siginifica a tela.kv, ids todos
        self.ids["moeda1"].text = f"Dólar: R${self.pegar_meme('USD')}"
        self.ids["moeda2"].text = f"Euro: R${self.pegar_meme('EUR')}"
        self.ids["moeda3"].text = f"Bitcoin: R${self.pegar_meme('BTC')}"

    def pegar_meme(self, moeda):
        link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()
        cotacao = dic_requisicao[f"{moeda}BRL"]["bid"]
        return cotacao

class MainApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Main1(name='main1'))
        sm.add_widget(Main2(name='main2'))
        return sm

if __name__ == "__main__":
    MainApp().run()

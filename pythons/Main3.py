from kivy.uix.screenmanager import Screen, ScreenManager
import requests
class Main3(Screen):
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
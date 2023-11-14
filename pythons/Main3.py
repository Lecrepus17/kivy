from kivy.uix.screenmanager import Screen
import requests
class Main3(Screen):
    def on_enter(self):
        # Este método é chamado quando a tela é exibida

        # Atualiza os textos dos widgets com as cotações das moedas
        self.ids["moeda1"].text = f"Dólar: R${self.pegar_cotacao('USD')}"
        self.ids["moeda2"].text = f"Euro: R${self.pegar_cotacao('EUR')}"
        self.ids["moeda3"].text = f"Bitcoin: R${self.pegar_cotacao('BTC')}"

    def pegar_cotacao(self, moeda):
        # Realiza uma requisição à API para obter a cotação da moeda em relação ao Real (BRL)
        link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        requisicao = requests.get(link)

        # Converte a resposta para um dicionário
        dic_requisicao = requisicao.json()

        # Extrai a cotação da moeda do dicionário
        cotacao = dic_requisicao[f"{moeda}BRL"]["bid"]

        return cotacao

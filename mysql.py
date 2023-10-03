import mysql.connector
# importes do kivy, app
from kivy.app import App
from kivy.lang import Builder
#import mysql.connector

# define "rotas para carregar páginas"
GUI = Builder.load_file("mysql.kv")

#  todo aplicativo é criado dentro de uma classe, orientação a objeto,
#  configura as funções, cada função define a função do aplicativo
class MeuAplicativo(App):
    # define função de Build, de criação def = function
    def build(self): # quando ele cria o app
        mydb = mysql.connector.connect(

        )
    # retorna a rota da tela
        return GUI


MeuAplicativo().run()

# importes do kivy, app
from kivy.app import App
from kivy.lang import Builder
import mysql.connector
# define "rotas para carregar páginas"
GUI = Builder.load_file("mysql.kv")

#  todo aplicativo é criado dentro de uma classe, orientação a objeto,
#  configura as funções, cada função define a função do aplicativo
class MeuAplicativo(App):
    # define função de Build, de criação def = function
    def build(self): # quando ele cria o app
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "",
        )
        c = mydb.cursor("CREATE DATABASE IF NOT EXISTS python17")

        c.execute("SHOW DATABASES")
        for db in c:
            print(db)

        c.execute()


    # retorna a rota da tela
        return GUI


MeuAplicativo().run()

# importes do kivy, app
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
import mysql.connector

Window.clearcolor = (14/255,61/255,76/255,1)
Window.size = (400,600)
# define "rotas para carregar páginas"
class Main1(BoxLayout):
    def adicionar(self):
        return 'alse'


class Main(App):
    def build(self):
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            database = "python1",
        )
        c = mydb.cursor()
        c.execute("CREATE DATABASE IF NOT EXISTS python1")

        c.execute("""CREATE TABLE if not exists mensagem(
            name VARCHAR(50))
        """)
        mydb.commit()
        mydb.close()
        return Main1()

Main().run()

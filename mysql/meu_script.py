
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
            database = "python171",
        )
        c = mydb.cursor()
        c.execute("CREATE DATABASE IF NOT EXISTS python171")

        c.execute("""CREATE TABLE if not exists clientes(
            name VARCHAR(50))
        """)
        mydb.commit()
        mydb.close()
    # retorna a rota da tela
        return GUI
    def submit(self):
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            database = "python171",
        )
        c = mydb.cursor()
        sql_command = "INSERT INTO clientes (name) VALUES (%s)"
        values = (self.root.ids.word_input.text,)
        c.execute(sql_command, values)
        mydb.commit()
        mydb.close()
    def show(self):
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            database = "python171",
        )
        c = mydb.cursor()
        c.execute("SELECT * FROM clientes")
        records = c.fetchall()
        word = ''
        for record in records:
            word = f'{word}\n{record[0]}'
            self.root.ids.word_label.text = f'{word}'
        mydb.commit()
        mydb.close()

MeuAplicativo().run()
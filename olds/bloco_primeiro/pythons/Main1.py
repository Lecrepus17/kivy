# Importe o módulo os para manipulação de arquivos
import os

from kivy.uix.screenmanager import Screen

class Main1(Screen):
    def save(self):
        # Obtém o texto inserido nos widgets com os ids "name" e "text"
        name = str(self.ids["name"].text)
        text = str(self.ids["text"].text)

        # Verifica se o nome está vazio e atribui 'name_null' nesse caso
        if not name:
            name = 'name_null'

        # Verifica se o texto está vazio e atribui 'text_null' nesse caso
        if not text:
            text = 'text_null'

        # Atualiza os widgets com os ids "name_final" e "text_final" com os valores obtidos
        self.ids["name_final"].text = name
        self.ids["text_final"].text = text

        # Diretório onde os arquivos serão salvos
        save_directory = "saves"

        # Verifica se o diretório 'saves' existe, se não existir, cria
        if not os.path.exists(save_directory):
            os.makedirs(save_directory)

        # Caminho completo dos arquivos
        nome_file_path = os.path.join(save_directory, "nome.txt")
        texto_file_path = os.path.join(save_directory, "texto.txt")

        # Escreve o nome no arquivo 'nome.txt' em uma nova linha
        with open(nome_file_path, 'a') as nome_file:
            nome_file.write(name + '\n')

        # Escreve o texto no arquivo 'texto.txt' em uma nova linha
        with open(texto_file_path, 'a') as texto_file:
            texto_file.write(text + '\n')


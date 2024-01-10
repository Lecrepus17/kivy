# Importe o módulo os para manipulação de arquivos
import os

from kivy.uix.screenmanager import Screen

class List(Screen):
    def on_enter(self):
        # Diretório onde os arquivos são salvos
        save_directory = "saves"

        # Caminho completo dos arquivos
        nome_file_path = os.path.join(save_directory, "nome.txt")
        texto_file_path = os.path.join(save_directory, "texto.txt")

        # Lista para armazenar os dados
        entries_list = []

        # Verifica se os arquivos existem
        if not os.path.exists(save_directory) or not os.path.exists(texto_file_path) or not os.path.exists(nome_file_path):
            # Se algum dos arquivos ou a pasta não existir, adicione uma entrada padrão
            entries_list.append({'text': 'Nenhum arquivo encontrado.'})
        else:
            # Lê as linhas dos arquivos
            with open(nome_file_path, 'r') as nome_file, open(texto_file_path, 'r') as texto_file:
                nomes = nome_file.readlines()
                textos = texto_file.readlines()

            # Verifica se há entradas nos arquivos
            if not nomes or not textos:
                # Se algum dos arquivos estiver vazio, adicione uma entrada padrão
                entries_list.append({'text': 'Nenhuma entrada encontrada.'})
            else:
                # Combina os nomes e textos e retorna a lista
                entries_list = [{'text': f"{nome.strip()}: {texto.strip()}"} for nome, texto in zip(nomes, textos)]

        # Atualiza o RecycleView com os dados
        rv_entries = self.ids['rv_entries']
        rv_entries.data = entries_list

import requests
import json
import urllib
import os
import tkinter as tk
from PIL import Image, ImageTk
from dotenv import load_dotenv
from threading import Thread
from time import sleep

load_dotenv()

class Twitter:
    def __init__(self, root):
        self.root = root
        self.root.title("Twitter Bio Checker")

        # Carrega a imagem de fundo
        self.background_image = Image.open("1.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        # Cria um Label para exibir a imagem de fundo
        self.background_label = tk.Label(root, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.username_label = tk.Label(root, text="Insira o @ que você quer buscar a bio:", font=("Helvetica", 16))
        self.username_label.pack(pady=(20, 0))  # Espaço no topo

        self.username_entry = tk.Entry(root, font=("Helvetica", 14), width=30)
        self.username_entry.pack(pady=10)  # Espaço após o campo de entrada

        self.check_button = tk.Button(root, text="Verificar Bio", command=self.check_bio, font=("Helvetica", 12), padx=10, pady=5)
        self.check_button.pack(pady=10)  # Espaço após o botão

        self.bio_text = tk.Text(root)
        self.bio_text.pack()

        self._json = TwitterJson()
        self._headers = {
            "Authorization": os.getenv("BEARER"),
            "X-CSRF-Token": os.getenv("CSRF")
        }
        self._cookies = {
            "cookie": os.getenv("COOKIE")
        }

        # Inicia um loop de atualização em uma thread
        self.update_thread = Thread(target=self.poll_bio_changes)
        self.update_thread.daemon = True
        self.update_thread.start()

    def check_bio(self):
        username = self.username_entry.get().replace("@", "")
        base_url = f"https://twitter.com/i/api/graphql/SAMkL5y_N9pmahSw8yy6gw/UserByScreenName?variables=%7B%22screen_name%22%3A%22{username}%22%2C%22withSafetyModeUserFields%22%3Atrue%7D&features={self._json['features']}&fieldToggles={self._json['fieldToggles']}"

        request = requests.get(base_url, headers=self._headers, cookies=self._cookies)

        try:
            data = request.json()
            if len(data['data']) == 0:
                self.bio_text.insert(tk.END, f"@{username} não existe.")
                return

            description = data['data']['user']['result']['legacy']['description']
            if len(description) == 0:
                self.bio_text.insert(tk.END, f"@{username} não possui uma descrição.")

            if description is not None:
                self.bio_text.insert(tk.END, f"Usuário: @{username}\nBio Atual: {description}\n\n")

        except Exception as e:
            self.bio_text.insert(tk.END, str(e))

    def poll_bio_changes(self):
        last_bio = ""  # Bio anterior
        while True:
            username = self.username_entry.get().replace("@", "")
            base_url = f"https://twitter.com/i/api/graphql/SAMkL5y_N9pmahSw8yy6gw/UserByScreenName?variables=%7B%22screen_name%22%3A%22{username}%22%2C%22withSafetyModeUserFields%22%3Atrue%7D&features={self._json['features']}&fieldToggles={self._json['fieldToggles']}"

            request = requests.get(base_url, headers=self._headers, cookies=self._cookies)

            try:
                data = request.json()
                if len(data['data']) == 0:
                    current_bio = f"@{username} não existe."
                else:
                    description = data['data']['user']['result']['legacy']['description']
                    current_bio = f"Usuário: @{username}\nBio Atual: {description}\n\n"

                # Atualiza a interface se a bio mudou
                if current_bio != last_bio:
                    last_bio = current_bio
                    self.root.after(0, self.update_bio_text, current_bio)

            except Exception as e:
                self.root.after(0, self.update_bio_text, str(e))

            # Aguarda um intervalo antes de verificar novamente
            sleep(10)  # Aguarda 10 segundos

    def update_bio_text(self, text):
        self.bio_text.delete("1.0", tk.END)  # Limpa o conteúdo atual
        self.bio_text.insert(tk.END, text)

def TwitterJson() -> object:
    with open('default.json') as params:
        data = json.load(params)
        features = data['features']
        fieldToggles = data['fieldToggles']

        return {
            "features": urllib.parse.quote(json.dumps(features)),
            "fieldToggles": urllib.parse.quote(json.dumps(fieldToggles))
        }

root = tk.Tk()
app = Twitter(root)
root.geometry("700x600")  # Defina o tamanho da janela
root.mainloop()

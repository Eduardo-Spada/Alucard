from flask import Flask
from threading import Thread
import requests
import time
import os
import bot  # Importa o bot.py

app = Flask('')

@app.route('/')
def home():
    return "O bot tá vivo, Felipe!"

@app.route('/healthz')
def health():
    return "OK", 200

def ping_self():
    while True:
        try:
            requests.get("https://pet-battle-system-code.onrender.com")  # Substitua pela URL do Render
        except:
            pass
        time.sleep(600)

def manter_vivo():
    port = int(os.environ.get("PORT", 8080))
    t1 = Thread(target=app.run, kwargs={'host': '0.0.0.0', 'port': port})
    t1.start()

if __name__ == '__main__':
    manter_vivo()
    bot.run_bot()

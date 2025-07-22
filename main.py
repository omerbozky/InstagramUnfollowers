from flask import Flask
from threading import Thread
import telebot

app = Flask('')

@app.route('/')
def home():
    return "Bot aktif."

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

BOT_TOKEN = "7827990578:AAEo4uYudHkvItgTDwIw0-KncSMDYi2Fjko"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "✅ Merhaba! Bot Render'da 7/24 çalışıyor.")

keep_alive()
bot.infinity_polling()

import qrcode
import telebot
import requests

bot = telebot.TeleBot('TOKEN')
last_message = None


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'سلام هر پیام ارسال کنی\nبرات کد qr می فرسته')

@bot.message_handler(func=lambda message: True)
def qr(message):
    global last_message
    if message.text != "/start":
        last_message = message.text
        img = qrcode.make(last_message)
        img.save("qr.png")
        with open("qr.png", "rb") as photo:
            bot.send_photo(message.chat.id, photo)



bot.polling()


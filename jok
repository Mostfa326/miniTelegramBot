#این وب سرویسی که من گذاشتم جوک هاش واقعا به مزست اگه مشگلی داشتید خودتون بگردید دنبال وب سرویس
import telebot
import requests

bot = telebot.TeleBot('7781513009:AAEFJGF46xE4FE8iHMZjNE3ZYgvY4VE7RSE')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'سلام هر پیام ارسال کنی برات جوک می فرسته')

@bot.message_handler(func=lambda message: True)
def jok(message):
    url = 'https://api.codebazan.ir/jok'
    response = requests.get(url, timeout=5)
    if response.status_code == 200:
        text = response.text
        bot.send_message(message.chat.id, text)
    else:
        bot.send_message(message.chat.id,'خطا در دریافت جوک از سرور')


bot.polling()



from telebot import TeleBot
from num2words import num2words

bot = TeleBot("TOKEN")


@bot.message_handler(func=lambda message: message.text.isdigit())
def rial_to_toman(message):
    rial = int(message.text)


    toman = rial // 10

    toman_words = num2words(toman, lang='fa')

    reply = f"{toman_words} تومان)"
    bot.reply_to(message, reply)


bot.infinity_polling()

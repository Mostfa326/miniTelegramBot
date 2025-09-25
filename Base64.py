import telebot
import base64

TOKEN = "TOKEN"
bot = telebot.TeleBot(TOKEN, parse_mode="Markdown")

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id,"Please send a text\nلطفا یک متن ارسال کنید")

def is_base64(s: str) -> bool:

    try:
        return base64.b64encode(base64.b64decode(s)).decode() == s
    except Exception:
        return False

@bot.message_handler(func=lambda m: True)
def handle_message(message):
    user_text = message.text.strip()

    if is_base64(user_text):

        try:
            decoded_text = base64.b64decode(user_text).decode("utf-8")
            bot.send_message(message.chat.id, f"```\n{decoded_text}\n```", parse_mode="Markdown")
        except Exception:
            bot.send_message(message.chat.id, "The text is not valid\nمتن معتبر نیست")
    else:

        encoded_text = base64.b64encode(user_text.encode("utf-8")).decode("utf-8")
        bot.send_message(message.chat.id, f"```\n{encoded_text}\n```", parse_mode="Markdown")


bot.infinity_polling()

import telebot
from telebot import types
import requests
import time

TOKEN = ''
Bot = telebot.TeleBot(TOKEN)

#توکن رو می تونید از وب سروریس نوسان بگیرید در غیر اینصورت کار نمی کنه
NAVASAN_API_KEY = ""
NAVASAN_URL = f"https://api.navasan.tech/latest/?api_key={NAVASAN_API_KEY}"


user_last_request = {}


markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
markup.add(
    types.KeyboardButton("قیمت دلار💲"),
    types.KeyboardButton("قیمت طلا🪙"),
    types.KeyboardButton("قیمت سایر ارز ها💰")
)

def _fmt_num(x):

    try:
        return f"{int(str(x).replace(',', '').strip()):,}"
    except Exception:
        return str(x)

def check_rate_limit(message):

    user_id = message.from_user.id
    now = time.time()
    last_time = user_last_request.get(user_id, 0)
    if now - last_time < 10:
        return False
    user_last_request[user_id] = now
    return True

@Bot.message_handler(commands=['start'])
def start(message):
    Bot.send_message(
        message.chat.id,
        "سلام به ربات قیمت لحظه‌ای خوش آمدید🌹\nاز منوی زیر استفاده کنید:",
        reply_markup=markup
    )


@Bot.message_handler(func=lambda m: m.text == "قیمت دلار💲")
def send_dollar(message):
    if not check_rate_limit(message):
        Bot.send_message(message.chat.id, "⏳ لطفا ۱۰ ثانیه صبر کنید و دوباره تلاش کنید.")
        return
    try:
        data = requests.get(NAVASAN_URL, timeout=10).json()
        buy = data.get("harat_naghdi_buy", {}).get("value")
        sell = data.get("harat_naghdi_sell", {}).get("value")
        time_stamp = data.get("harat_naghdi_buy", {}).get("date")

        if buy and sell:
            text = (
                "💵 قیمت لحظه‌ای دلار (بازار آزاد):\n"
                f"🔹 خرید: {_fmt_num(buy)} تومان\n"
                f"🔸 فروش: {_fmt_num(sell)} تومان\n"
                f"⏰ آخرین بروزرسانی: {time_stamp}"
            )
        else:
            text = "❌ اطلاعات دلار پیدا نشد."
    except Exception as e:
        text = f"❌ خطا در دریافت اطلاعات:\n{e}"

    Bot.send_message(message.chat.id, text)

# 📌 دکمه طلا (فقط طلای ۱۸ عیار)
@Bot.message_handler(func=lambda m: m.text == "قیمت طلا🪙")
def send_gold(message):
    if not check_rate_limit(message):
        Bot.send_message(message.chat.id, "⏳ لطفا ۱۰ ثانیه صبر کنید و دوباره تلاش کنید.")
        return
    try:
        data = requests.get(NAVASAN_URL, timeout=10).json()
        gold18 = data.get("18ayar", {}).get("value")
        time_stamp = data.get("18ayar", {}).get("date")

        if gold18:
            text = (
                "🪙 قیمت طلا:\n"
                f"🔹 طلای ۱۸ عیار: {_fmt_num(gold18)} تومان\n"
                f"⏰ آخرین بروزرسانی: {time_stamp}"
            )
        else:
            text = "❌ اطلاعات طلا پیدا نشد."
    except Exception as e:
        text = f"❌ خطا در دریافت اطلاعات:\n{e}"

    Bot.send_message(message.chat.id, text)

# 📌 دکمه سایر ارزها (۱۰ ارز برتر)
@Bot.message_handler(func=lambda m: m.text == "قیمت سایر ارز ها💰")
def send_other_currencies(message):
    if not check_rate_limit(message):
        Bot.send_message(message.chat.id, "⏳ لطفا ۱۰ ثانیه صبر کنید و دوباره تلاش کنید.")
        return
    try:
        data = requests.get(NAVASAN_URL, timeout=10).json()

        currencies = {
            "eur": "🇪🇺 یورو",
            "gbp": "🇬🇧 پوند انگلیس",
            "jpy": "🇯🇵 ین ژاپن",
            "cny": "🇨🇳 یوان چین",
            "chf": "🇨🇭 فرانک سوئیس",
            "cad": "🇨🇦 دلار کانادا",
            "aud": "🇦🇺 دلار استرالیا",
            "aed": "🇦🇪 درهم امارات",
            "try": "🇹🇷 لیر ترکیه",
            "rub": "🇷🇺 روبل روسیه"
        }

        text = "💰 قیمت سایر ارزها:\n\n"
        found = False
        for key, label in currencies.items():
            val = data.get(key, {}).get("value")
            if val:
                found = True
                text += f"{label}: {_fmt_num(val)} تومان\n"

        if not found:
            text = "❌ اطلاعات ارزها پیدا نشد."
    except Exception as e:
        text = f"❌ خطا در دریافت اطلاعات:\n{e}"

    Bot.send_message(message.chat.id, text)

Bot.polling(none_stop=True)

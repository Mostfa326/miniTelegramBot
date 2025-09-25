import telebot
import jdatetime
import pytz
from datetime import datetime

TOKEN = "TOKEN"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(func=lambda m: True)
def send_time(message):
    
    tz = pytz.timezone("Asia/Tehran")
    now = datetime.now(tz)

    
    time_str = now.strftime("%H:%M:%S")

    
    j_now = jdatetime.datetime.fromgregorian(datetime=now)
    date_str = j_now.strftime("%Y/%m/%d")
    weekday = j_now.strftime("%A")  

    
    days_fa = {
        "Saturday": "شنبه",
        "Sunday": "یکشنبه",
        "Monday": "دوشنبه",
        "Tuesday": "سه‌شنبه",
        "Wednesday": "چهارشنبه",
        "Thursday": "پنجشنبه",
        "Friday": "جمعه"
    }
    weekday_fa = days_fa.get(weekday, weekday)

    
    bot.send_message(
        message.chat.id,
        f"🕒 ساعت: `{time_str}`\n📅 تاریخ: `{date_str}`\n📌 روز: {weekday_fa}\n🌍 منطقه زمانی: Asia/Tehran",
        parse_mode="Markdown"
    )


bot.infinity_polling()

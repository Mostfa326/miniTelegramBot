import telebot
from telebot.types import ReplyKeyboardMarkup
from telebot import types
import imageio
from PIL import Image
import os
#import VideoFileClip from*

TOKEN = 'TOKEN'
bot = telebot.TeleBot(TOKEN)


#----------------------------------------منو اصلی----------------------------
markup = types.ReplyKeyboardMarkup(resize_keyboard=True , row_width=1)
steker_btn = types.KeyboardButton("تبدیل عکس به استیکر📷")
gif_btn = types.KeyboardButton("تبدیل عکس به گیف🖼")
rahnma_btn = types.KeyboardButton("تبدیل ویدیو کوتاه به گیف🎞")
markup.add(steker_btn, gif_btn , rahnma_btn )

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'سلام به ربات تبدیل خوش آمدید\nاز دکمه های زیر استفاده کنید',reply_markup=markup)


#------------------------------------------------------------تبدیل عکس به استیکر--------------------------------
@bot.message_handler(func=lambda message: message.text == "تبدیل عکس به استیکر📷")
def handle_sticker_request(message):
    bot.send_message(message.chat.id, "لطفاً عکس‌تون رو ارسال کنید تا تبدیلش کنم به استیکر 😄")

    @bot.message_handler(content_types=['photo'])
    def convert_photo_to_sticker(message):
        
        file_info = bot.get_file(message.photo[-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        
        with open("temp_image.png", 'wb') as new_file:
            new_file.write(downloaded_file)

        
        with open("temp_image.png", 'rb') as sticker_file:
            bot.send_sticker(message.chat.id, sticker_file)

#------------------------------------------------------------تبدیل عکس به گیف--------------------------------

@bot.message_handler(func=lambda message: message.text == "تبدیل عکس به گیف🖼")
def handle_gif_request(message):
    bot.send_message(message.chat.id, "لطفاً عکس‌تون رو ارسال کنید تا تبدیلش کنم به گیف 🎬")

    @bot.message_handler(content_types=['photo'])
    def convert_photo_to_gif(message):
        
        file_info = bot.get_file(message.photo[-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        
        image_path = "temp_image.jpg"
        with open(image_path, 'wb') as new_file:
            new_file.write(downloaded_file)

        
        img = Image.open(image_path)

        
        frames = [img.copy() for _ in range(5)] 

        
        gif_path = "output.gif"
        imageio.mimsave(gif_path, frames, duration=0.3)

        
        with open(gif_path, 'rb') as gif_file:
            bot.send_document(message.chat.id, gif_file)

        
        os.remove(image_path)
        os.remove(gif_path)

#------------------------------------------------------------تبدیل ویدیو کوتاه به گیف--------------------------------

@bot.message_handler(func=lambda message: message.text == "تبدیل ویدیو کوتاه به گیف🎞")
def handle_video_to_gif(message):
    bot.send_message(message.chat.id, "این بخش در حال آپدیت است لطفا از بقیه بخش های ربات استفاده کنید")



bot.polling()

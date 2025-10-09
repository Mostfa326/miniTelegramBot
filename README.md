<h1 align="center">🤖 Mini Telegram Bots | ربات‌های کوچک تلگرام</h1>

<p align="center">
  <a href="#english">🌍 English</a> | <a href="#فارسی">🇮🇷 فارسی</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python" alt="Python Badge"/>
  <img src="https://img.shields.io/badge/Telegram-Bots-blue?logo=telegram" alt="Telegram Badge"/>
  <img src="https://img.shields.io/badge/Library-TeleBot-green" alt="TeleBot Badge"/>
</p>

<hr/>

## 🌍 English

Hello 👋  
Welcome to **Mini Telegram Bots**!  
Here I share some of my small Telegram bots that I build in my free time.  
Most of them are written using the `TeleBot` library (also known as `pyTelegramBotAPI`).  

Each bot is designed to be **simple, clean, and beginner-friendly**, so you can easily understand, edit, and use them in your own projects. 🚀  

### ✨ Features
- Simple and readable Python code  
- Built with `TeleBot` (pyTelegramBotAPI)  
- Perfect for learning or small personal projects  
- Open source — you can use and modify the code freely  

### 📂 Example Code
```python
import telebot

bot = telebot.TeleBot("YOUR_TOKEN_HERE")

@bot.message_handler(commands=['start'])
def start(msg):
    bot.send_message(msg.chat.id, "Hello! 👋 Welcome to Mini Bots.")

bot.polling()

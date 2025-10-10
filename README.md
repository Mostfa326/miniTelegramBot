<!doctype html>
<html lang="fa" dir="rtl">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>🤖 ربات‌های کوچک تلگرام | Mini Telegram Bots</title>
  <style>
    :root{--bg:#0f1724;--card:#0b1220;--muted:#94a3b8;--accent:#06b6d4}
    body{font-family:system-ui,-apple-system,'Segoe UI',Roboto,'Helvetica Neue',Tahoma;line-height:1.6;margin:0;background:linear-gradient(180deg,#071229 0%,#061322 100%);color:#e6eef6;padding:24px}
    .container{max-width:900px;margin:20px auto;padding:24px;background:rgba(255,255,255,0.02);border-radius:12px;box-shadow:0 6px 30px rgba(2,6,23,0.6)}
    header{text-align:center;margin-bottom:18px}
    h1{margin:6px 0;font-size:28px}
    .lang-links{margin:8px 0}
    .badges img{height:28px;margin:4px}
    hr{border:none;border-top:1px solid rgba(255,255,255,0.06);margin:18px 0}
    h2{font-size:18px;margin:12px 0}
    p{color:var(--muted);margin:8px 0}
    pre{background:#061826;padding:12px;border-radius:8px;overflow:auto;color:#dff3fb}
    code{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,'Liberation Mono',monospace}
    .center{display:flex;justify-content:center}
    a.button{display:inline-block;background:rgba(6,182,212,0.12);color:var(--accent);padding:8px 12px;border-radius:8px;text-decoration:none;border:1px solid rgba(6,182,212,0.12)}
    footer{margin-top:18px;text-align:center;color:rgba(255,255,255,0.35);font-size:13px}
  </style>
</head>
<body>
  <div class="container">
    <header>
      <h1>🤖 ربات‌های کوچک تلگرام | Mini Telegram Bots</h1>
      <div class="lang-links">
        <a href="#english">🌍 English</a> | <a href="#فارسی">🇮🇷 فارسی</a>
      </div>
      <div class="badges center">
        <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python" alt="Python Badge">
        <img src="https://img.shields.io/badge/Telegram-Bots-blue?logo=telegram" alt="Telegram Badge">
        <img src="https://img.shields.io/badge/Library-TeleBot-green" alt="TeleBot Badge">
      </div>
    </header>

    <hr>

    <section id="فارسی">
      <h2>🇮🇷 فارسی</h2>
      <p>سلام 👋<br>به <strong>ربات‌های کوچک تلگرام</strong> خوش اومدی! اینجا چند تا از ربات‌های کوچیکی که در اوقات فراغتم می‌سازم رو به اشتراک می‌ذارم. بیشترشون با استفاده از کتابخونه‌ی <code>TeleBot</code> (همون <code>pyTelegramBotAPI</code>) نوشته شدن.</p>
      <p>هر ربات به‌صورت <strong>ساده، تمیز و مناسب برای مبتدی‌ها</strong> طراحی شده تا بتونی راحت کدش رو بخونی، ویرایشش کنی و در پروژه‌هات ازش استفاده کنی. 🚀</p>

      <h3>✨ ویژگی‌ها</h3>
      <ul>
        <li>کد پایتون ساده و قابل فهم</li>
        <li>ساخته شده با <code>TeleBot</code> (pyTelegramBotAPI)</li>
        <li>مناسب برای یادگیری یا پروژه‌های شخصی کوچک</li>
        <li>متن‌باز — می‌تونی آزادانه از کدها استفاده یا اون‌ها رو ویرایش کنی</li>
      </ul>

      <h3>📂 نمونه کد</h3>
      <pre><code>import telebot

bot = telebot.TeleBot("توکن_خودت_را_اینجا_بگذار")

@bot.message_handler(commands=['start'])
def start(msg):
    bot.send_message(msg.chat.id, "سلام! 👋 به ربات‌های کوچک خوش اومدی.")

bot.polling()
</code></pre>
    </section>

    <hr>

    <section id="english">
      <h2>🌍 English</h2>
      <p>Hello 👋<br>Welcome to <strong>Mini Telegram Bots</strong>! Here I share some of my small Telegram bots that I build in my free time. Most of them are written using the <code>TeleBot</code> library (also known as <code>pyTelegramBotAPI</code>).</p>
      <p>Each bot is designed to be <strong>simple, clean, and beginner-friendly</strong>, so you can easily understand, edit, and use them in your own projects. 🚀</p>

      <h3>✨ Features</h3>
      <ul>
        <li>Simple and readable Python code</li>
        <li>Built with <code>TeleBot</code> (pyTelegramBotAPI)</li>
        <li>Perfect for learning or small personal projects</li>
        <li>Open source — you can use and modify the code freely</li>
      </ul>

      <h3>📂 Example Code</h3>
      <pre><code>import telebot

bot = telebot.TeleBot("YOUR_TOKEN_HERE")

@bot.message_handler(commands=['start'])
def start(msg):
    bot.send_message(msg.chat.id, "Hello! 👋 Welcome to Mini Bots.")

bot.polling()
</code></pre>
    </section>

    <footer>
     
    </footer>
  </div>
</body>
</html>

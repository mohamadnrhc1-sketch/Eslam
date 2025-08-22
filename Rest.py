
# bot by NADAR 🤍
import telebot
from telebot import types
from PIL import Image, ImageDraw, ImageFont
import random
import string
import time
import threading
import os


BOT_TOKEN = "7583122312:AAGzfFwAHoI_i_ygVmCjv9ao3fehwA3U95g"
CHANNEL_LINK = "https://t.me/ge5_z1"
ALLOWED_USER_ID = 8388988847

bot = telebot.TeleBot(BOT_TOKEN)
active_users = {}
used_users = set()

def generate_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

def generate_image(text, filename='code.png'):
    img = Image.new('RGB', (300, 100), color=(255, 255, 255))
    d = ImageDraw.Draw(img)
    font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    font = ImageFont.truetype(font_path, 36)
    d.text((50, 30), text, font=font, fill=(0, 0, 0))
    img.save(filename)

def remove_user_after_delay(user_id, delay=300):
    time.sleep(delay)
    if user_id in active_users:
        del active_users[user_id]

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_id = message.from_user.id
    if user_id in used_users:
        bot.send_message(user_id, "متكدر تدخل بعد انتهت المحاولات فرصة سعيدًا العزيز .")
        return

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("بلش تحقق .", callback_data='start_verify'))
    bot.send_message(user_id, "- هلا العزيز بنظام حماية قناتك او قناة ثانية

- بكل بساطة هذه خادمك يساعدك من سبام لقناتك والبوتات .

- كل الي عليك بس اضغط زر الادناه للبدء وشوف السيد وين يوديك", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'start_verify')
def handle_verify(call):
    user_id = call.from_user.id
    if user_id in used_users:
        bot.send_message(user_id, "لا يمكنك تحقق مره اخرى .")
        return

    code = generate_code()
    active_users[user_id] = code
    generate_image(code)

    with open("code.png", "rb") as photo:
        bot.send_photo(user_id, photo, caption="اكتب الكود الاعلى الي بالصوره")

    
    threading.Thread(target=remove_user_after_delay, args=(user_id,)).start()

@bot.message_handler(func=lambda m: m.from_user.id in active_users)
def handle_code(message):
    user_id = message.from_user.id
    code_entered = message.text.strip()

    if code_entered != active_users[user_id]:
        bot.send_message(user_id, "رمز غلط.")
        return

    del active_users[user_id]
    used_users.add(user_id)

    bot.send_message(user_id, "تم تحقق من انك لست روبوت بنجاح .\n\nهذه الرابط صالح لمدة 5 دقائق وثم تنتهي صلاحيتة .\n\nالرابط: " + CHANNEL_LINK)

bot.polling()


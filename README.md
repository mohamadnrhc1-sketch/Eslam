import os
from pyrogram import Client, filters
from pyrogram.types import Message

# Replace with your actual Bot Token
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7583122312:AAF9f7U_f2L1ZpKIu09_1JHfvLYGts1jVOI")
# Replace with your actual API ID and API Hash
API_ID = os.environ.get("API_ID", "28792492")
API_HASH = os.environ.get("API_HASH", "3f0db7e7472b764058e6aeb37265f69d")

# Create a new Pyrogram client
app = Client("my_bot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

@app.on_message(filters.command("start"))
def start_command(client, message: Message):
    message.reply_text("أهلًا بك! أنا بوت موسيقى. أرسل لي رابط أغنية من يوتيوب أو سبوتيفاي وسأقوم بتشغيلها لك.")

# Start the bot
print("Bot is starting...")
app.run()

from telegram import Bot
from datetime import datetime
import pytz
import os

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=TOKEN)

today = datetime.now(pytz.timezone("Asia/Tehran"))
date_text = today.strftime("📅 امروز:\n%Y/%m/%d")

bot.send_message(chat_id=CHAT_ID, text=date_text)

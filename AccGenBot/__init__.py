from telethon import TelegramClient
from Configs import Config
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

bot = TelegramClient("bot", api_id=Config.APP_ID, api_hash=Config.API_HASH)
AccGenBot = bot.start(bot_token=Config.TOKEN)


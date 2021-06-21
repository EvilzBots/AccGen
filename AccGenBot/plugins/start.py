from . import *
from .. import *
from telethon import Button, events
from telethon.tl.functions.users import GetFullUserRequest
from Configs import Config

@AccGenBot.on(events.NewMessage(pattern="/start"))
async def start(event):

    await event.reply(f"**Heya\n\nWelcome to AccGenBot, From Here You can Generate free Accounts\n\nMade With ❤️ By @EvilzBots**", buttons=[[Button.inline("Generate Accounts", data="gen")], [Button.url("Join Channel!", Config.CHANNEL_URL)]])

#Repeat Codes :/
@AccGenBot.on(events.callbackquery.CallbackQuery(data=b"start_bot"))
async def start(event):

    await event.reply(f"**Heya \n\nWelcome to AccGenBot, From Here You can Generate free Accounts\n\nMade With ❤️ By @EvilzBots**", buttons=[[Button.inline("Generate Accounts", data="gen")], [Button.url("Join Channel!", Config.CHANNEL_URL)]])

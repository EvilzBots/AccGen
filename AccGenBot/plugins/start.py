from . import *
from .. import *
from telethon import Button, events
from telethon.tl.functions.users import GetFullUserRequest
from Configs import Config

@AccGenBot.on(events.NewMessage(pattern="/start"))
async def start(event):

    evil = await verify(Config.CHANNEL_US, event, AccGenBot)
    if evil is False:
            await event.reply("**Join my channel to use this bot :)**", buttons=[[Button.url("Join Channel", Config.CHANNEL_URL)]])
            return

    name = heck.user.first_name
    await event.reply(f"**Heya\n\nWelcome to AccGenBot, From Here You can Generate free Accounts\n\nMade With ❤️ By @EvilzBots**", buttons=[[Button.inline("Generate Accounts", data="gen")], [Button.url("Join Channel!", Config.CHANNEL_URL)]])

#Repeat Codes :/
@AccGenBot.on(events.callbackquery.CallbackQuery(data=b"start_bot"))
async def start(event):

    evil = await verify(Config.CHANNEL_US, event, AccGenBot)
    if evil is False:
            await event.edit("**Join my channel to use this bot :)**", buttons=[[Button.url("Join Channel", Config.CHANNEL_URL)]])
            return

    name = heck.user.first_name
    await event.reply(f"**Heya \n\nWelcome to AccGenBot, From Here You can Generate free Accounts\n\nMade With ❤️ By @EvilzBots**", buttons=[[Button.inline("Generate Accounts", data="gen")], [Button.url("Join Channel!", Config.CHANNEL_URL)]])

from . import *
from .. import *
from telethon import Button, events
from telethon.tl.functions.users import GetFullUserRequest
from Configs import Config

@AccGenBot.on(events.NewMessage(pattern="/start"))
async def start(event):

    await AccGenBot.send_message(Config.PRV_CHAT, f"Bot Started By [{event.sender_id}](tg://user?id={event.sender_id})")
    evil = await verify(Config.CHANNEL_US, event, AccGenBot)
    if evil is False:
            await event.reply("**Join my channel to use this bot :)**", buttons=[[Button.url("Join Channel", Config.CHANNEL_URL)]])
            return

    heck = await AccGenBot(GetFullUserRequest(event.sender_id))
    name = heck.user.first_name
    await event.reply(f"**Heya {name}\the
#Repeat Codes :/
@AccGenBot.on(events.callbackquery.CallbackQuery(data=b"start_bot"))
async def start(event):

    evil = await verify(Config.CHANNEL_US, event, AccGenBot)
    if evil is False:
            await event.edit("**Join my channel to use this bot :)**", buttons=[[Button.url("Join Channel", Config.CHANNEL_URL)]])
            return

    heck = await AccGenBot(GetFullUserRequest(event.sender_id))
    name = heck.user.first_name
    await event.reply(f"**Heya {name}\n\nI am Account Generator Bot.\n\nType /cmds to know the available the Commands!\n\n❤️ I'm Made By @EvilzBots**", buttons=[[Button.inline("Generate Accounts", data="gen")], [Button.url("Join Channel!", Config.CHANNEL_URL)]])

@AccGenBot.on(events.NewMessage(pattern="/cmds"))
async def cmds(event):

    evil = await verify(Config.CHANNEL_US, event, AccGenBot)
    if evil is False:
            await event.edit("**Join my channel to use this bot :)**", buttons=[[Button.url("Join Channel", Config.CHANNEL_URL)]])
            return

    heck = await AccGenBot(GetFullUserRequest(event.sender_id))
    name = heck.user.first_name
    await event.reply(f"**/zee5**", buttons=[[Button.inline("Generate Accounts", data="gen")], [Button.url("Join Channel!", Config.CHANNEL_URL)]])

from . import *
from .. import *
from Configs import Config
from telethon import Button, events
from telethon.tl.functions.users import GetFullUserRequest
import random
from lists import users

@AccGenBot.on(events.NewMessage(pattern="/zee5"))
async def zee5(event):
    chat = event.sender_id
    evil = await verify(Config.CHANNEL_US, event, AccGenBot)

    if evil is False:
           await event.reply("**Join my channel to use me :)**", buttons=[[Button.url("Join Channel", Config.CHANNEL_URL)]])
           return
    try:
        if users[chat]:
            users[chat] += 1
    except:
        users[chat] = 1

    hehe = await event.edit("<b><i>Generating Account</i></b>", parse_mode="HTML")

    if users[chat] <= 5:
        with open('firstacc.txt') as ha:
            sedloif = ha.read().splitlines()
        sed = random.choice(sedloif)
        user_s = await AccGenBot.get_me()
        user_us = user_s.username
        email, password = sed.split(":")

        await hehe.edit(f"**Zee5 Account\n\nCombo: `{email}`:`{password}`\nEmail: `{email}`\nPassword: `{password}`\n\nGenerated By: @{event.sender.username}\nUser-ID: {event.sender_id}\nLimit Remained= {5-users[chat]}**",
    buttons=[
        [Button.url("Join Channel", Config.CHANNEL_URL)],
        [Button.inline("Generate Again", data="gen")]
    ])
    else:
        await hehe.edit("Limit Exceed")

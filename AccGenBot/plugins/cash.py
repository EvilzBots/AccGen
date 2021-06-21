import random
from . import *
from .. import *
from telethon import events
from telethon import Button
from telethon.tl.functions.users import GetFullUserRequest
from Configs import Config

@AccGenBot.on(events.callbackquery.CallbackQuery(data=b"cash"))
async def sad(event):
    text="**Choose The Which Account You Want**"
    await event.edit(text,
                     buttons=[
                         [Button.inline("✘ Wish ✘", data="wish")],
                         [Button.inline("✘ Bitcoin Blast ✘", data="bbc")],
                         [Button.inline("Main Menu", data="gen")]
                     ])

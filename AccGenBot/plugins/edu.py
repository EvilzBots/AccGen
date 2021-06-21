import random
from . import *
from .. import *
from telethon import events
from telethon import Button
from telethon.tl.functions.users import GetFullUserRequest
from Configs import Config

@AccGenBot.on(events.callbackquery.CallbackQuery(data=b"edu"))
async def sed(event):
    text="*Choose The Which Account You Want*"
    await event.edit(text,
                     buttons=[
                         [Button.inline("✘ KhanAcademy ✘", data="khan")],
                         [Button.inline("✘ UnAcademy ✘", data="unac")],
                         [Button.inline("Main Menu", data="gen")]
                     ])

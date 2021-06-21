import random
from . import *
from .. import *
from telethon import events
from telethon import Button
from telethon.tl.functions.users import GetFullUserRequest
from Configs import Config

@AccGenBot.on(events.callbackquery.CallbackQuery(data=b"stream"))
async def sad(event):
    text="*Choose The Which Account You Want*"
    await event.edit(text,
                     buttons=[
                         [Button.inline("✘ Netflix ✘", data="netflix"), Button.inline("✘ Voot ✘", data="voot")],
                         [Button.inline("✘ Zee5 ✘", data="zee5"), Button.inline("✘ AltBalaji ✘", data="altb")],
                         [Button.inline("✘ Aha ✘", data="aha")],
                         [Button.inline("Main Menu", data="gen")]
                     ])

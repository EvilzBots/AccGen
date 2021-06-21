import random
from . import *
from .. import *
from telethon import events
from telethon import Button
from telethon.tl.functions.users import GetFullUserRequest
from Configs import Config

@AccGenBot.on(events.callbackquery.CallbackQuery(data=b"vpns"))
async def sed(event):
    text="*Choose The Vpn Which You Want*"
    await event.edit(text,
                     buttons=[
                         [Button.inline("✘ Nord Vpn ✘", data="nord")],
                         [Button.inline("✘ IpVanish ✘", data="ips")],
                         [Button.inline("Main Menu", data="gen")]
                     ])

from telethon import Button, custom, events
import telethon
from telethon.tl.functions.channels import GetParticipantRequest


async def verify(channel_id, event, bot):
    try:
            result = await bot(
                functions.channels.GetParticipantRequest(
                    channel=channel_id, user_id=event.sender_id
                )
            )
            if result.participant:
                return True
    except telethon.errors.rpcerrorlist.UserNotParticipantError:
        return False

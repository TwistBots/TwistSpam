from .. import Riz, SUDO_USERS, twistversion
from .. import ALIVE_PIC
from telethon import events, version, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime

RIZ_PIC = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/c1d95129f334e29ed4776.jpg"
  

          
twist = "• `Twist Spam Is Alive` •\n\n"

twist += f"┏━━━━━━━━━━━━━━━━━━━\n"

twist += f"┣➣ **Ping ** : `3.9.6`\n"

twist += f"┣➣ **Bot Version** : `{version.__version__}`\n"

twist += f"┣➣ **Twist Version**  : `{twistversion}`\n"

twist += f"┗━━━━━━━━━━━━━━━━━━━\n\n"
         
                                    
@Riz.on(events.NewMessage(pattern=".alive"))
async def alive(event):
    if event.sender_id in SUDO_USERS:
     await Riz.send_file(event.chat_id,
                                  RIZ_PIC,
                                  caption=twist,
                                  buttons=[
        [
        Button.url("Channel", "https://t.me/TwistSupport"),
        Button.url("Chats", "https://t.me/TwistChats")
        ],
        [
        Button.url("< Repo >", "https://github.com/TwistBots/TwistSpam")
        ]
        ]
        )
    

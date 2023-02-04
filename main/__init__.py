#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 25355159
API_HASH = "d0e845f6e9f32a42f9f52f091df9e952" 
BOT_TOKEN = "6097902087:AAGTmB9zfaebMbNWRBchtJ2T2vzxkYUmhxI"
SESSION ="BQC5LBLqtU1ycD41Il69zmJe4-VDURCR4Q9AuvwlYJEXFWkpQ8XwwraWzIGH4hbXXllC-GBKJ6srZ37-vMMz1UQlzIp6N86-ftzQXgEe0n9CGFGFkbP2_D3lt-NG6JryI5g0hdtQ9g-32YmZwwy2-fySwxHB6g58mFVWBjV7g3DCl6jG2KD3Dc2k-CxwmPBr1wsOrHuZ0VMP9S4M9i-2-rq-YyAylm78K06No-V7rs8s6LkdeDq3WwYB_mSAK0OIyU2r6k0rejPcxlDGC200K2-vwrLpXm6C_U7pb-tXKYKV8Tatpm3C4uuglMYlW5TbKxAstgcJa0wA2H0CUBd7_8a7fY91MQA"
FORCESUB ="hornypostmax"
AUTH = 2106553649, 5909582134, 5204618807

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)

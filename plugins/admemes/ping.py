"""Telegram Ping / Pong Speed
Syntax: .ping"""

import time
import random
from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.helper_functions.cust_p_filters import f_onw_fliter

# -- Constants -- #
ALIVE = "ചത്തിട്ടില്ല മുത്തേ ഇവിടെ തന്നെ ഉണ്ട്..😇  എങ്കിലും ചുമ്മാ ഒന്ന് /help ചെയ്തു നോക്ക്..🙂" 
REPO = "Sorry This bot is  Not a open source bot"
CHANNEL = "⚙️"
PIRATE = "Hi, Guys I'am a Developer, If You Need A Bot Like This => PM ME @PiratesDeveloper I Will Also Develope Bot Like Mallu_Movies/ProSearch bot and We Will Also Develope Bot As Your Wish😇"
# -- Constants End -- #


@Client.on_message(filters.command("alive", COMMAND_HAND_LER) & f_onw_fliter)
async def check_alive(_, message):
    await message.reply_text(ALIVE)


@Client.on_message(filters.command("ping", COMMAND_HAND_LER) & f_onw_fliter)
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")


@Client.on_message(filters.command("repo", COMMAND_HAND_LER) & f_onw_fliter)
async def repo(_, message):
    await message.reply_text(REPO)


@Client.on_message(filters.command("group", COMMAND_HAND_LER) & f_onw_fliter)
async def group(_, message):
    await message.reply_text(GROUP)
    
    
@Client.on_message(filters.command("clone", COMMAND_HAND_LER) & f_onw_fliter)
async def check_alive(_, message):
    await message.reply_text(PIRATE)







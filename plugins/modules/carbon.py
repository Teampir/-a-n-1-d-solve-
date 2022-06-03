from pyrogram import filters
from aiohttp import ClientSession
from pyrogram import Client as bot
from plugins.function import make_carbon
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
aiohttpsession = ClientSession()

C = "MADE BY => [Pirate Team](https://t.me/AdBotUpdate)"
F = InlineKeyboardMarkup(
[[
     InlineKeyboardButton("ᴜᴩᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ", url="https://t.me/AdBotUpdate")
]]
)




@bot.on_message(filters.command("carbon"))
async def carbon_func(_, message):
    if not message.reply_to_message:
        return await message.reply_text(
            "ʀᴇᴩʟᴀy ᴛᴏ ᴀɴy ᴛᴇxᴛ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴍᴀᴋᴇ ᴄᴀʀʙᴏɴ...❄️"
        )
    if not message.reply_to_message.text:
        return await message.reply_text(
            "ʀᴇᴩʟᴀy ᴛᴏ ᴀɴy ᴛᴇxᴛ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴍᴀᴋᴇ ᴄᴀʀʙᴏɴ...❄️"
        )
    user_id = message.from_user.id
    m = await message.reply_text("ᴄʀᴇᴀᴛɪɴɢ...🎭")
    carbon = await make_carbon(message.reply_to_message.text)
    await m.edit("ᴜᴩʟᴏᴀʀᴅɪɴɢ...")
    await message.reply_photo(
        photo=carbon,
        caption=C,
        reply_markup=F)
    await m.delete()
    carbon.close()
